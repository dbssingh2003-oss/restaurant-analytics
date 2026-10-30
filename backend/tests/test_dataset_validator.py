
import pandas as pd

from app.services.dataset_validator import validate_dataset


def test_valid_dataset():
    df = pd.DataFrame({
        "order_id": [101, 102],
        "order_date": ["2026-01-01", "2026-01-02"],
        "quantity": [2, 3],
        "unit_price": [150, 200],
    })

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is True
    assert result.row_count == 2
    assert result.errors == []


def test_missing_required_column():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["2026-01-01"],
        "quantity": [2],
    })

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is False
    assert "unit_price" in result.missing_columns


def test_empty_dataset():
    df = pd.DataFrame(columns=[
        "order_id",
        "order_date",
        "quantity",
        "unit_price",
    ])

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is False
    assert result.row_count == 0


def test_invalid_date():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["invalid-date"],
        "quantity": [2],
        "unit_price": [150],
    })

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is False
    assert any("invalid dates" in error for error in result.errors)


def test_zero_quantity():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["2026-01-01"],
        "quantity": [0],
        "unit_price": [150],
    })

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is False
    assert "Quantity must be greater than zero." in result.errors


def test_negative_unit_price():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["2026-01-01"],
        "quantity": [2],
        "unit_price": [-150],
    })

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is False
    assert "Unit price cannot be negative." in result.errors


def test_non_numeric_quantity():
    df = pd.DataFrame({
        "order_id": [101],
        "order_date": ["2026-01-01"],
        "quantity": ["abc"],
        "unit_price": [150],
    })

    result = validate_dataset(df, "sales.csv")

    assert result.is_valid is False
    assert any("non-numeric" in error for error in result.errors)

