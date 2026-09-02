# Predictive Analytics Using Historical Data

## Thiranex Data Analytics Internship - Task 3

### Project Overview

This project focuses on predictive analytics using historical monthly sales data. A Linear Regression model is used to analyze historical sales patterns and forecast future sales for 2026.

### Objectives

- Clean and preprocess historical sales data
- Analyze historical sales trends
- Build a predictive regression model
- Evaluate model performance
- Forecast future sales
- Visualize actual and predicted sales

### Dataset

The dataset contains monthly sales records from January 2024 to December 2025.

Columns:

- Month - Month and year of the sales record
- Sales - Monthly sales value
- Month_Number - Numerical representation of time used by the model

### Data Preprocessing

The following preprocessing steps were performed:

1. Converted the Month column into datetime format.
2. Checked for missing values.
3. Checked for duplicate records.
4. Created a numerical Month_Number feature.
5. Divided the data into training and testing sets.

### Machine Learning Model

A Linear Regression model was used to predict future sales.

The first 80% of the historical observations were used for training, while the remaining 20% were used for testing.

### Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE): 139.45
- Root Mean Squared Error (RMSE): 163.57
- R² Score: 0.23

### Forecasting

The trained model was used to forecast monthly sales for all 12 months of 2026.

The predicted sales show an overall increasing trend based on the historical data.

### Visualizations

The project includes:

- Historical Monthly Sales
- Actual vs Predicted Sales
- 2026 Sales Forecast
- Historical Sales and 2026 Forecast

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- GitHub

### Project Files

- `sales_data.csv` - Historical sales dataset
- `predictive_sales.py` - Python source code
- `requirements.txt` - Required Python libraries
- `historical_sales.png` - Historical sales visualization
- `actual_vs_predicted.png` - Actual vs predicted sales
- `2026_sales_forecast.png` - 2026 forecast visualization
- `historical_and_forecast.png` - Combined historical and forecast visualization

### Conclusion

The project demonstrates how historical sales data can be used to build a predictive analytics solution. Linear Regression was applied to identify the relationship between time and sales and generate future sales forecasts for 2026.

