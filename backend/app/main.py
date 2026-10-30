
from fastapi import FastAPI

from app.api.router import router
from app.core.config import (
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
)

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Register API routes under /api/v1
app.include_router(router, prefix="/api/v1")


@app.get("/")
def home():
    return {
        "message": "Welcome to the Restaurant Intelligence Platform API",
        "status": "running",
    }
