
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_valid_csv_upload():
    csv_content = (
        b"order_id,order_date,quantity,unit_price\n"
        b"101,2026-01-01,2,150\n"
        b"102,2026-01-02,3,200\n"
    )

    response = client.post(
        "/api/v1/datasets/validate",
        files={
            "file": (
                "sales.csv",
                csv_content,
                "text/csv",
            )
        },
    )

    assert response.status_code == 200
    assert response.json()["is_valid"] is True
    assert response.json()["row_count"] == 2


def test_csv_with_missing_column():
    csv_content = (
        b"order_id,order_date,quantity\n"
        b"101,2026-01-01,2\n"
    )

    response = client.post(
        "/api/v1/datasets/validate",
        files={
            "file": (
                "sales.csv",
                csv_content,
                "text/csv",
            )
        },
    )

    assert response.status_code == 200
    assert response.json()["is_valid"] is False
    assert "unit_price" in response.json()["missing_columns"]


def test_reject_non_csv_file():
    response = client.post(
        "/api/v1/datasets/validate",
        files={
            "file": (
                "sales.txt",
                b"sample data",
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Please upload a CSV file."
