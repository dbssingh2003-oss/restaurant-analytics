
import pandas as pd
from pandas import DataFrame

from app.schemas.analytics import (
    AnalyticsResponse,
    DailyRevenue,
    PerformanceItem,
)


def _get_top_performers(
    df: DataFrame,
    column: str,
) -> list[PerformanceItem]:

    if column not in df.columns:
        return []

    data = df.copy()
    data[column] = data[column].fillna("Unknown").astype(str)

    grouped = (
        data.groupby(column, as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            quantity_sold=("quantity", "sum"),
        )
        .sort_values("revenue", ascending=False)
        .head(5)
    )

    return [
        PerformanceItem(
            name=str(row[column]),
            revenue=float(row["revenue"]),
            quantity_sold=float(row["quantity_sold"]),
        )
        for _, row in grouped.iterrows()
    ]


def calculate_analytics(
    df: DataFrame,
    filename: str,
) -> AnalyticsResponse:

    # Normalize column names.
    data = df.copy()
    data.columns = [
        str(column).strip().lower()
        for column in data.columns
    ]

    required_columns = [
        "order_id",
        "order_date",
        "quantity",
        "unit_price",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )

    if data.empty:
        raise ValueError("Dataset contains no data rows.")

    # Convert columns to appropriate data types.
    data["quantity"] = pd.to_numeric(
        data["quantity"],
        errors="raise",
    )

    data["unit_price"] = pd.to_numeric(
        data["unit_price"],
        errors="raise",
    )

    data["order_date"] = pd.to_datetime(
        data["order_date"],
        errors="raise",
    )

    # Calculate revenue for every sales row.
    data["revenue"] = (
        data["quantity"] * data["unit_price"]
    )

    # Calculate overall business metrics.
    total_revenue = float(data["revenue"].sum())

    order_count = int(data["order_id"].nunique())

    average_order_value = (
        total_revenue / order_count
        if order_count > 0
        else 0.0
    )

    # Calculate revenue for each day.
    data["order_day"] = (
        data["order_date"].dt.strftime("%Y-%m-%d")
    )

    daily_summary = (
        data.groupby("order_day", as_index=False)
        .agg(revenue=("revenue", "sum"))
    )

    daily_revenue = [
        DailyRevenue(
            order_date=row["order_day"],
            revenue=float(row["revenue"]),
        )
        for _, row in daily_summary.iterrows()
    ]

    # Calculate top products and categories.
    top_products = _get_top_performers(
        data,
        "product_name",
    )

    top_categories = _get_top_performers(
        data,
        "category",
    )

    return AnalyticsResponse(
        filename=filename,
        total_revenue=total_revenue,
        order_count=order_count,
        average_order_value=average_order_value,
        daily_revenue=daily_revenue,
        top_products=top_products,
        top_categories=top_categories,
    )
