
# System Architecture

## 1. Frontend
Technology: React + Vite

Responsibilities:
- CSV upload interface
- Data preview
- Analytics dashboard
- Forecast charts
- Report export

## 2. Backend
Technology: Python + FastAPI

Responsibilities:
- Validate uploaded data
- Calculate business metrics
- Run forecasting operations
- Generate reports
- Return results through REST APIs

## 3. Data and Machine Learning
- Pandas for data processing
- scikit-learn for model training and evaluation
- SQLite or PostgreSQL for persistent records when implemented

## 4. Communication
The frontend sends HTTP requests to the backend REST API.
The backend validates requests and returns structured responses.

## 5. Security
- Validate file types and file sizes
- Never commit secrets
- Handle uploaded data safely
- Add authentication before supporting multiple users

## 6. Deployment
Deploy the frontend and backend as separate services when practical.
Configure environment variables and verify the live application.
