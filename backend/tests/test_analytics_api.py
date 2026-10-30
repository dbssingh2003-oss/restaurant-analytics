
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_analytics_api_with_valid_csv():
    csv_content = (
        b"order_id,order_date,quantity,unit_price\n"
        b"101,2026-01-01,2,150\n"
        b"102,2026-01-02,3,200\n"
        b"103,2026-01-03,1,100\n"
        b"104,2026-01-04,5,250\n"
        b"105,2026-01-05,2,300\n"
    )

    response = client.post(
        "/api/v1/analytics",
        files={
            "file": (
                "restaurant_sales.csv",
                csv_content,
                "text/csv",
            )
        },
    )

    assert response.status_code == 200

    result = response.json()

    assert result["total_revenue"] == 2850
    assert result["order_count"] == 5
    assert result["average_order_value"] == 570
    assert len(result["daily_revenue"]) == 5


def test_analytics_api_rejects_invalid_dataset():
    csv_content = (
        b"order_id,order_date,quantity\n"
        b"101,2026-01-01,2\n"
    )

    response = client.post(
        "/api/v1/analytics",
        files={
            "file": (
                "invalid_sales.csv",
                csv_content,
                "text/csv",
            )
        },
    )

    assert response.status_code == 422
    assert "unit_price" in response.json()["detail"]["missing_columns"]
