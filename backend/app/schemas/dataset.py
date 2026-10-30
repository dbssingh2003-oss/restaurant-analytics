
from pydantic import BaseModel, Field


class DatasetValidationResponse(BaseModel):
    filename: str
    is_valid: bool
    row_count: int
    column_count: int

    missing_columns: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
