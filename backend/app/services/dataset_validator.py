
from pandas import DataFrame, to_datetime, to_numeric

from app.schemas.dataset import DatasetValidationResponse


REQUIRED_COLUMNS = [
    "order_id",
    "order_date",
    "quantity",
    "unit_price",
]


def validate_dataset(
    df: DataFrame,
    filename: str
) -> DatasetValidationResponse:

    normalized_df = df.copy()

    normalized_df.columns = [
        str(column).strip().lower()
        for column in df.columns
    ]

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in normalized_df.columns
    ]

    errors = []
    warnings = []

    # Check required columns
    if missing_columns:
        errors.append(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )

    # Check empty dataset
    if df.empty:
        errors.append(
            "The uploaded dataset contains no data rows."
        )

    # Validate dates and numeric values
    if not missing_columns and not df.empty:

        invalid_dates = to_datetime(
            normalized_df["order_date"],
            errors="coerce"
        ).isna()

        if invalid_dates.any():
            errors.append(
                "Column 'order_date' contains invalid dates."
            )

        for column in ["quantity", "unit_price"]:

            values = to_numeric(
                normalized_df[column],
                errors="coerce"
            )

            if values.isna().any():
                errors.append(
                    f"Column '{column}' contains "
                    "non-numeric or missing values."
                )

            if column == "quantity" and (
                values.dropna() <= 0
            ).any():
                errors.append(
                    "Quantity must be greater than zero."
                )

            if column == "unit_price" and (
                values.dropna() < 0
            ).any():
                errors.append(
                    "Unit price cannot be negative."
                )

    return DatasetValidationResponse(
        filename=filename,
        is_valid=len(errors) == 0,
        row_count=len(df),
        column_count=len(df.columns),
        missing_columns=missing_columns,
        errors=errors,
        warnings=warnings,
    )

