
import pandas as pd
import pytest

from app.services.analytics_service import calculate_analytics


def test_calculate_analytics():
    df = pd.DataFrame({
        "order_id": [101, 101, 102, 103],
        "order_date": [
            "2026-01-01",
            "2026-01-01",
            "2026-01-02",
            "2026-01-02",
        ],
        "quantity": [2, 1, 3, 2],
        "unit_price": [100, 50, 200, 150],
        "product_name": [
            "Burger",
            "Fries",
            "Burger",
            "Pizza",
        ],
        "category": [
            "Meals",
            "Sides",
            "Meals",
            "Meals",
        ],
    })

    result = calculate_analytics(df, "sales.csv")

    assert result.total_revenue == pytest.approx(1150)
    assert result.order_count == 3
    assert result.average_order_value == pytest.approx(1150 / 3)

    assert len(result.daily_revenue) == 2

    assert result.daily_revenue[0].revenue == pytest.approx(250)
    assert result.daily_revenue[1].revenue == pytest.approx(900)

    assert result.top_products[0].name == "Burger"
    assert result.top_products[0].revenue == pytest.approx(800)

    assert result.top_categories[0].name == "Meals"
    assert result.top_categories[0].revenue == pytest.approx(1100)


def test_analytics_without_optional_columns():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["2026-01-01"],
        "quantity": [2],
        "unit_price": [150],
    })

    result = calculate_analytics(df, "sales.csv")

    assert result.total_revenue == 300
    assert result.top_products == []
    assert result.top_categories == []


def test_analytics_missing_required_column():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["2026-01-01"],
        "quantity": [2],
    })

    with pytest.raises(ValueError, match="unit_price"):
        calculate_analytics(df, "sales.csv")


def test_analytics_empty_dataset():
    df = pd.DataFrame(columns=[
        "order_id",
        "order_date",
        "quantity",
        "unit_price",
    ])

    with pytest.raises(
        ValueError,
        match="Dataset contains no data rows",
    ):
        calculate_analytics(df, "sales.csv")
