# Restaurant Intelligence Platform — Data Schema

## 1. Purpose

This document defines the structure, data types, and validation rules for restaurant sales CSV files accepted by the platform.

## 2. Data Design Principles

- Each row represents one order line, not necessarily one complete order.
- An order may contain multiple products, so an order ID may appear in multiple rows.
- Revenue is calculated from quantity multiplied by unit price unless a separate line-total field is provided and validated.
- Missing or invalid values must be handled explicitly.
- Forecasting requires valid dates and sufficient historical data.
- The application must not assume that every uploaded dataset has product or category information.

## 3. Supported Columns

| Column | Data Type | Required | Description |
|---|---|---|---|
| order_id | String | Yes | Unique identifier for an order; may repeat across different order lines. |
| order_date | Date or datetime | Yes | Date and optional time when the order was placed. |
| product_name | String | No | Name of the product sold. |
| category | String | No | Product category. |
| quantity | Positive number | Yes | Number of units sold in the order line. |
| unit_price | Non-negative number | Yes | Price per unit in the dataset's currency. |
| total_amount | Non-negative number | No | Optional line total. If supplied, validate it against quantity multiplied by unit price, subject to documented discounts or adjustments. |

## 4. Minimum Required Columns

The minimum supported CSV must contain:

- order_id
- order_date
- quantity
- unit_price

Product analysis requires product_name or category.

The platform must not silently invent missing values for required business fields.

## 5. Example CSV

```csv
order_id,order_date,product_name,category,quantity,unit_price,total_amount
ORD001,2026-01-01,Burger,Main Course,2,150.00,300.00
ORD001,2026-01-01,Cold Coffee,Beverage,1,80.00,80.00
ORD002,2026-01-02,Pizza,Main Course,1,250.00,250.00
ORD003,2026-01-02,Lemon Soda,Beverage,3,50.00,150.00
ORD004,2026-01-03,Sandwich,Snacks,2,100.00,200.00
```

The example uses a generic currency. The application must not assume a currency symbol unless the user specifies the currency.

## 6. Validation Rules

### File validation

- Accept CSV files only.
- Reject empty files and files without a valid header.
- Enforce a configurable upload-size limit.
- Handle malformed rows with clear error messages.

### Column validation

- Confirm that all required columns exist.
- Trim unnecessary whitespace from headers and text values.
- Reject duplicate column names after normalization.
- Parse order_date into a valid date or datetime.
- Ensure quantity is numeric and greater than zero.
- Ensure unit_price is numeric and non-negative.
- Ensure required order IDs are present.
- Flag missing or invalid values with useful row-level feedback.

### Business validation

- An order ID may occur in multiple rows because one order can contain multiple products.
- Revenue must be calculated consistently at the order-line level.
- If total_amount is supplied, validate its relationship with quantity and unit_price. Explain any mismatch rather than silently changing the data.
- Refunds, taxes, discounts, and cancellation records require explicit handling if they appear in future datasets.
- Duplicate-looking rows should be flagged or assessed carefully; do not automatically delete them without a defined rule.

## 7. Derived Metrics

### Line revenue

If there are no discounts or adjustments:

Line Revenue = Quantity × Unit Price

### Total revenue

Total Revenue = Sum of valid line revenue across the selected dataset.

### Order count

Order Count = Number of distinct valid order IDs.

### Average order value

Average Order Value = Total Revenue ÷ Number of distinct valid orders.

If the number of valid orders is zero, average order value must be reported as unavailable rather than dividing by zero.

### Daily revenue

Daily Revenue = Sum of line revenue for each calendar date.

## 8. Forecasting Requirements

- Aggregate validated line revenue by date before forecasting.
- Use chronological training and test periods to avoid future-data leakage.
- Check whether the dataset has sufficient dates and observations.
- Explain when forecasting cannot be performed reliably.
- Report forecast evaluation metrics separately from optimizer comparison metrics.

## 9. Error Reporting

The application should report:

- Missing required columns
- Invalid dates
- Non-numeric or invalid quantities and prices
- Missing order IDs
- Malformed CSV records
- Insufficient historical data for forecasting
- Revenue inconsistencies when an optional total_amount is supplied

Messages should explain the problem and, where practical, identify affected row numbers.

## 10. Future Extensions

Future versions may support restaurant location, payment method, discount amount, tax amount, refund status, order status, and currency. These fields should only be introduced when their business definitions and validation rules are documented.
