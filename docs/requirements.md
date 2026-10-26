# Software Requirements Specification (SRS)

## 1. Project Overview

**Project Name:** Restaurant Intelligence Platform

**Project Type:** Full-stack web application for restaurant analytics, revenue forecasting, and optimization experiments.

### 1.1 Purpose

The application will transform restaurant sales data into meaningful business insights using data analysis, interactive visualizations, and machine learning.

### 1.2 Problem Statement

Restaurant owners and managers may struggle to understand sales performance, identify top-selling products, recognize trends, and estimate future revenue using raw transaction data.

### 1.3 Proposed Solution

The platform will allow users to upload restaurant sales data, validate it, explore key business metrics, forecast revenue when sufficient historical data is available, compare optimization algorithms, and export results.

## 2. Target Users

- Restaurant owners and managers
- Business analysts
- Data science learners and developers

## 3. Functional Requirements

| ID | Requirement | Expected Behavior |
|---|---|---|
| FR-01 | CSV Upload | Upload a supported restaurant sales CSV file. |
| FR-02 | Data Validation | Check required columns, data types, missing values, and invalid records. |
| FR-03 | KPI Analytics | Calculate total revenue, order count, and average order value. |
| FR-04 | Sales Trends | Visualize revenue and sales over time. |
| FR-05 | Product Analysis | Identify top products and categories when relevant columns exist. |
| FR-06 | Revenue Forecasting | Forecast daily revenue when sufficient historical data exists. |
| FR-07 | Forecast Evaluation | Report MAE and RMSE using a chronological test set. |
| FR-08 | Optimizer Comparison | Compare Gradient Descent, Adam, and Newton's method on the same objective function. |
| FR-09 | Optimization Visualization | Show loss, iterations, convergence behavior, and execution time. |
| FR-10 | Result Export | Download supported analysis and forecast results. |
| FR-11 | Error Handling | Explain invalid files, missing fields, and insufficient data clearly. |

## 4. Non-Functional Requirements

- **Usability:** Provide a clear and understandable dashboard.
- **Performance:** Process reasonable CSV files without unnecessary delays.
- **Reliability:** Handle invalid input without crashing.
- **Maintainability:** Keep frontend, backend, analytics, and machine-learning modules organized.
- **Security:** Validate uploads, restrict file size and type, and avoid exposing internal errors.
- **Testability:** Include automated tests for core business logic and API behavior.
- **Portability:** Document local setup and deployment instructions.

## 5. Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, Vite, TypeScript |
| Styling | Tailwind CSS |
| Charts | Plotly |
| Backend | Python, FastAPI |
| Data Processing | Pandas, NumPy |
| Forecasting | Scikit-learn |
| Optimization | NumPy and SciPy, as appropriate |
| Initial Data Handling | In-memory processing |
| Optional Persistence | SQLite |
| Testing | Pytest and suitable frontend testing tools |
| Version Control | Git and GitHub |
| CI | GitHub Actions |

## 6. Project Scope

### Included in the MVP

- CSV upload and validation
- Business KPI calculations
- Sales trend visualization
- Product and category analysis when supported by the data
- Revenue forecasting and evaluation
- Optimization algorithm comparison
- Result export
- Automated tests and documentation
- Deployment, subject to the available timeline

### Excluded from the Initial MVP

- Live point-of-sale integration
- Real-time restaurant monitoring
- Payment processing
- Enterprise user management
- Guaranteed forecasting accuracy
- Advanced authentication and persistent storage unless time permits

## 7. Assumptions and Constraints

- Users provide their own restaurant sales data.
- The dataset must contain the fields needed for the requested analysis.
- Forecasting requires a valid date field and sufficient historical observations.
- Product analysis requires product or category information.
- The system must explain when a requested analysis cannot be performed.
- The development schedule is 15 days, with approximately 1–2 hours available per day.

## 8. Acceptance Criteria

The MVP is accepted when:

1. A valid CSV file can be uploaded and processed.
2. Invalid input produces understandable error messages.
3. Supported KPIs are calculated correctly.
4. Available sales trends can be visualized.
5. Forecast evaluation uses a chronological training and test split.
6. Optimization algorithms are evaluated on the same objective function under documented conditions.
7. Supported results can be exported.
8. Relevant automated tests pass.
9. Setup instructions allow the project to run locally.
10. Documentation accurately describes supported features and limitations.

## 9. Evaluation Metrics

### Forecasting

- **MAE:** Mean Absolute Error between actual and predicted revenue.
- **RMSE:** Root Mean Squared Error, which penalizes larger prediction errors more heavily.

### Optimization

- Final objective-function loss
- Iterations required
- Execution time
- Convergence behavior

Forecast accuracy and optimizer convergence must be evaluated separately.

## 10. Future Enhancements

Possible future features include database persistence, authentication, evidence-based business recommendations, Docker, PostgreSQL, and additional forecasting models.
