# API Contract — Restaurant Intelligence Platform

## 1. Purpose

This document defines the initial REST API contract between the React frontend and the FastAPI backend.

## 2. API Conventions

- Base URL during local development: `http://localhost:8000`
- API prefix: `/api/v1`
- Data format: JSON for requests and responses, except file uploads and downloadable files.
- HTTP methods: GET for retrieval, POST for processing or creating results.
- Error responses should contain a clear message.
- Uploaded datasets are processed in memory in the initial MVP.

## 3. Endpoints

### 3.1 Health Check

**Endpoint:** `GET /health`

**Purpose:** Verify that the backend service is running.

**Example response:**

```json
{
  "status": "ok"
}
```

### 3.2 Upload and Validate CSV

**Endpoint:** `POST /api/v1/datasets/validate`

**Content type:** `multipart/form-data`

**Input:** A CSV file uploaded using the field name `file`.

**Purpose:** Check whether the dataset follows the supported data schema.

**Example success response:**

```json
{
  "valid": true,
  "row_count": 100,
  "columns": ["order_id", "order_date", "quantity", "unit_price"],
  "warnings": []
}
```

The values above are illustrative, not actual results.

### 3.3 Calculate Analytics

**Endpoint:** `POST /api/v1/analytics`

**Content type:** `multipart/form-data`

**Input:** A CSV file uploaded using the field name `file`.

**Purpose:** Calculate supported restaurant sales metrics.

**Example response:**

```json
{
  "total_revenue": 12500.0,
  "order_count": 85,
  "average_order_value": 147.06,
  "daily_revenue": [
    {
      "date": "2026-01-01",
      "revenue": 3800.0
    }
  ],
  "top_products": [],
  "top_categories": []
}
```

Example values are illustrative. Actual results depend on the uploaded dataset.

### 3.4 Forecast Revenue

**Endpoint:** `POST /api/v1/forecast`

**Content type:** `multipart/form-data`

**Input:** A CSV file and optional forecast settings.

**Purpose:** Forecast daily revenue when the dataset has sufficient valid historical observations.

**Illustrative response:**

```json
{
  "status": "success",
  "model": "baseline",
  "horizon_days": 7,
  "metrics": {
    "mae": 125.5,
    "rmse": 160.2
  },
  "predictions": [
    {
      "date": "2026-01-10",
      "predicted_revenue": 1750.0
    }
  ]
}
```

The model name, metrics, and prediction values shown here are examples only.

### 3.5 Compare Optimization Algorithms

**Endpoint:** `POST /api/v1/optimization/compare`

**Content type:** `application/json`

**Purpose:** Compare Gradient Descent, Adam, and Newton's method on the same documented objective function.

**Example request:**

```json
{
  "objective": "quadratic",
  "max_iterations": 100,
  "learning_rate": 0.01
}
```

**Illustrative response:**

```json
{
  "objective": "quadratic",
  "results": [
    {
      "algorithm": "Gradient Descent",
      "final_loss": 0.001,
      "iterations": 100,
      "execution_time_ms": 2.5,
      "converged": true
    }
  ]
}
```

The response will include a result for each algorithm actually executed. The values above are illustrative and must not be treated as measured performance.

### 3.6 Export Analytics

**Endpoint:** `POST /api/v1/analytics/export`

**Content type:** `multipart/form-data`

**Input:** A CSV file and an export format supported by the implementation.

**Purpose:** Return analysis results as a downloadable file, such as CSV.

## 4. Standard Error Response

Errors should use an appropriate HTTP status code and a consistent JSON structure.

**Example:**

```json
{
  "error": {
    "code": "INVALID_DATASET",
    "message": "The uploaded CSV is missing required columns.",
    "details": ["order_date"]
  }
}
```

## 5. Expected HTTP Status Codes

| Status | Meaning |
|---|---|
| 200 | Request processed successfully |
| 400 | Invalid request or dataset |
| 413 | Uploaded file exceeds the permitted size |
| 415 | Unsupported file type |
| 422 | Invalid parameters or validation failure |
| 500 | Unexpected server error |

FastAPI may return its own validation response format for some errors; the implementation should standardize responses where practical.

## 6. Data and Error Handling

- Validate every uploaded file before calculating analytics.
- Do not return stack traces or sensitive internal information to the client.
- Report missing columns and invalid records clearly.
- Do not silently replace invalid financial values.
- Return an informative response when forecasting is unsupported due to insufficient data.
- Keep forecasting evaluation separate from optimizer convergence results.

## 7. Implementation Notes

- These endpoints describe the planned API, not an implemented service.
- Exact parameter names and response schemas must be reflected in the FastAPI implementation.
- API tests should verify successful requests, invalid files, and insufficient data.
- If the same uploaded dataset must be reused across requests, persistent or temporary dataset identifiers may be introduced later.
