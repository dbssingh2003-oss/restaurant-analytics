
# Smart Restaurant Analytics & Revenue Prediction Platform

## 1. Project Overview
A full-stack web application that helps restaurant owners analyze sales data and forecast future revenue.

## 2. Problem Statement
Restaurant owners often maintain sales records in spreadsheets. Manually analyzing revenue trends and product performance takes time. This application will convert sales data into useful business insights.

## 3. Target Users
- Restaurant owners
- Restaurant managers

## 4. Functional Requirements
- FR-01: Upload a CSV sales file.
- FR-02: Validate columns, data types, and missing values.
- FR-03: Preview uploaded records.
- FR-04: Calculate revenue and order metrics.
- FR-05: Visualize daily and monthly sales trends.
- FR-06: Compare product and category performance.
- FR-07: Forecast future revenue using historical data.
- FR-08: Evaluate forecasting performance using appropriate metrics.
- FR-09: Export an analysis report.

## 5. Non-Functional Requirements
- NFR-01: Display understandable error messages.
- NFR-02: Separate frontend and backend responsibilities.
- NFR-03: Keep secrets out of source control.
- NFR-04: Test important business calculations.
- NFR-05: Document setup and execution.
- NFR-06: Handle empty or invalid datasets safely.

## 6. Technology Stack
- Frontend: React and Vite
- Backend: Python and FastAPI
- Data processing: Pandas and NumPy
- Charts: Plotly
- Machine learning: scikit-learn
- Version control: Git and GitHub
- Testing: Pytest
- Storage: CSV processing initially; SQLite or PostgreSQL when persistence is implemented

## 7. MVP Scope
The first version will support CSV upload, data validation, analytics, revenue forecasting, and report export.

Authentication, multi-restaurant access, and advanced inventory recommendations are future enhancements.

## 8. Success Criteria
- Valid CSV files can be analyzed.
- Invalid files produce useful errors.
- Dashboard metrics match verified calculations.
- Forecasts are evaluated on data not used for training.
- Core automated tests pass.
- The deployed app completes the primary workflow.
- A developer can follow the README to run the project.

## 9. Risks and Assumptions
Forecast quality depends on data quality, history, and sales patterns. Predictions are estimates, not guarantees. The first release is a demonstration and decision-support tool.

## 10. Future Improvements
- User authentication
- Persistent database storage
- Scheduled model retraining
- Inventory and staffing recommendations
