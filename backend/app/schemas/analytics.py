
from pydantic import BaseModel, Field


class DailyRevenue(BaseModel):
    order_date: str
    revenue: float


class PerformanceItem(BaseModel):
    name: str
    revenue: float
    quantity_sold: float


class AnalyticsResponse(BaseModel):
    filename: str

    total_revenue: float
    order_count: int
    average_order_value: float

    daily_revenue: list[DailyRevenue] = Field(
        default_factory=list
    )

    top_products: list[PerformanceItem] = Field(
        default_factory=list
    )

    top_categories: list[PerformanceItem] = Field(
        default_factory=list
    )
