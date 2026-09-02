
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create historical sales data
data = {
    "Month": [
        "2024-01", "2024-02", "2024-03", "2024-04",
        "2024-05", "2024-06", "2024-07", "2024-08",
        "2024-09", "2024-10", "2024-11", "2024-12",
        "2025-01", "2025-02", "2025-03", "2025-04",
        "2025-05", "2025-06", "2025-07", "2025-08",
        "2025-09", "2025-10", "2025-11", "2025-12"
    ],
    "Sales": [
        1200, 1350, 1280, 1450, 1520, 1600,
        1550, 1700, 1680, 1800, 1950, 2100,
        2050, 2200, 2150, 2350, 2450, 2500,
        2600, 2750, 2700, 2900, 3050, 3200
    ]
}

df = pd.DataFrame(data)

# Data preprocessing
df["Month"] = pd.to_datetime(df["Month"])
df["Month_Number"] = range(1, len(df) + 1)

# Prepare training and testing data
X = df[["Month_Number"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Results")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 2))

# Forecast 2026
future_months = pd.date_range(
    start="2026-01-01",
    periods=12,
    freq="MS"
)

future_month_numbers = range(len(df) + 1, len(df) + 13)

future_predictions = model.predict(
    pd.DataFrame({"Month_Number": future_month_numbers})
)

future_df = pd.DataFrame({
    "Month": future_months,
    "Predicted_Sales": future_predictions
})

print("\n2026 Sales Forecast")
print(future_df.to_string(index=False))
