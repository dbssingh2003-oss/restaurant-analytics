
import pandas as pd

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.dataset import DatasetValidationResponse
from app.services.dataset_validator import validate_dataset


router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "restaurant-analytics-backend",
    }


@router.post(
    "/datasets/validate",
    response_model=DatasetValidationResponse,
    tags=["Datasets"],
)
def validate_uploaded_dataset(file: UploadFile = File(...)):

    # Check the uploaded file extension.
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file.",
        )

    # Read the CSV file using Pandas.
    try:
        df = pd.read_csv(file.file)

    except pd.errors.EmptyDataError:
        raise HTTPException(
            status_code=400,
            detail="The uploaded CSV file is empty or has no header row.",
        )

    except (pd.errors.ParserError, UnicodeDecodeError):
        raise HTTPException(
            status_code=400,
            detail="The uploaded file could not be parsed as a valid CSV.",
        )

    # Validate the dataset.
    result = validate_dataset(
        df=df,
        filename=file.filename,
    )

    return result
