# Enterprise Demand Forecasting & Inventory Optimization

An end-to-end retail demand forecasting project that uses **Python, Machine Learning, and Power BI** to predict product demand and convert forecasts into actionable inventory recommendations.

The project covers the complete workflow from **data preparation and exploratory analysis to machine learning, model evaluation, demand forecasting, inventory optimization, and business reporting**.

---

## 📌 Project Overview

Accurate demand forecasting helps retailers reduce overstocking, avoid stockouts, and improve inventory planning.

This project uses historical retail sales data to:

* Analyze historical demand patterns
* Prepare and clean the data
* Engineer features for machine learning
* Train and compare multiple ML models
* Select the best-performing model
* Generate product-level demand forecasts
* Convert forecasts into inventory recommendations
* Present the results through an interactive Power BI dashboard

---

## 🚀 Project Workflow

```text
Raw Retail Data
       ↓
Data Preparation
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Best Model Selection
       ↓
Demand Forecasting
       ↓
Inventory Optimization
       ↓
Power BI Dashboard
```

---

## 📂 Project Structure

```text
Enterprise-Demand-Forecasting/
│
├── data/
│   ├── raw/
│   │   ├── sales_train_evaluation.csv
│   │   ├── calendar.csv
│   │   └── sell_prices.csv
│   │
│   └── processed/
│       └── features.parquet
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Preparation.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Training.ipynb
│   ├── 05_Model_Evaluation.ipynb
│   └── 06_Inventory_Optimization.ipynb
│
├── reports/
│   ├── forecast_results.csv
│   ├── inventory_recommendations.csv
│   ├── dashboard_data.csv
│   └── model_comparison.csv
│
├── PowerBI/
│   └── Enterprise_Demand_Forecasting.pbix
│
└── README.md
```

---

## 📊 Dataset

The project uses retail sales data containing:

* Product information
* Product categories
* Departments
* Store information
* State information
* Daily historical sales
* Calendar information
* Events
* Selling prices

The final modeling workflow was developed using **CA_1** as the selected store to keep the modeling process computationally manageable.

The selected dataset contains approximately **3,049 unique products**.

---

# 📓 Notebooks

## 01 — Exploratory Data Analysis

The EDA notebook investigates the structure and behavior of the dataset.

### Analysis includes:

* Dataset dimensions
* Column information
* Missing-value analysis
* Unique products
* Departments
* Categories
* Stores
* Sales trends
* Monthly sales
* Weekday patterns
* Category-level sales
* Department-level sales
* Event-related sales

The analysis helps identify important demand patterns before modeling.

---

## 02 — Data Preparation

The data preparation notebook converts the raw retail data into a clean dataset suitable for analysis and modeling.

### Main steps:

* Load raw sales, calendar, and price data
* Select the `CA_1` store
* Convert sales from wide format to long format
* Join sales with calendar information
* Join selling-price information
* Handle missing values
* Correct data types
* Prepare the cleaned dataset for feature engineering

---

## 03 — Feature Engineering

Feature engineering transforms the prepared dataset into model-ready features.

The process includes useful:

* Product features
* Category features
* Department features
* Store features
* Calendar features
* Price-related features
* Historical demand features

The resulting dataset is stored as:

```text
data/processed/features.parquet
```

Parquet was used to improve storage and processing efficiency for the large dataset.

---

## 04 — Model Training

Multiple models were trained to establish a baseline and compare different machine learning approaches.

### Models

* Linear Regression
* Random Forest
* XGBoost
* LightGBM
* CatBoost

The baseline model provides a reference point for evaluating whether the more advanced models provide meaningful improvements.

---

## 05 — Model Evaluation

The models were evaluated using:

* **MAE** — Mean Absolute Error
* **RMSE** — Root Mean Squared Error
* **R² Score** — Coefficient of Determination

### Model Results

| Model             |        MAE |       RMSE |   R² Score |
| ----------------- | ---------: | ---------: | ---------: |
| LightGBM          |     1.0346 | **2.0222** | **0.6564** |
| XGBoost           | **1.0333** |     2.0321 |     0.6530 |
| CatBoost          |     1.0546 |     2.0340 |     0.6524 |
| Random Forest     |     1.0948 |     2.0934 |     0.6318 |
| Linear Regression |     1.0668 |     2.1026 |     0.6285 |

### Best Model

**LightGBM** achieved the highest R² score (**0.6564**) and the lowest RMSE (**2.0222**).

XGBoost achieved the lowest MAE (**1.0333**).

Based on the overall evaluation, **LightGBM was selected for the final forecasting workflow**.

The evaluation notebook also includes **SHAP-based model explainability** to understand feature importance and model behavior.

---

## 06 — Inventory Optimization

The selected model is used to generate product-level demand forecasts.

The forecasting output contains:

```text
item_id
store_id
forecast_sales
```

The predicted demand is then converted into inventory recommendations:

```text
Increase Stock
Maintain Stock
Reduce Stock
```

The final outputs are saved in the `reports/` directory.

---

# 📦 Output Files

### `forecast_results.csv`

Contains product-level demand predictions.

```text
item_id
store_id
forecast_sales
```

### `inventory_recommendations.csv`

Contains forecasts along with inventory recommendations.

```text
item_id
store_id
forecast_sales
Recommendation
```

### `dashboard_data.csv`

Enriched dataset prepared for Power BI containing information such as:

```text
item_id
cat_id
dept_id
store_id
state_id
date
sell_price
forecast_sales
Recommendation
```

### `model_comparison.csv`

Contains the evaluation results of all trained models.

---

# 📊 Power BI Dashboard

The final results are presented through a **two-page Power BI dashboard**.

## Page 1 — Inventory Overview

The dashboard provides a high-level business view with:

* Total Products
* Average Forecast
* Increase Stock
* Recommendation Distribution
* Top 10 Products
* Forecast Sales by Category
* Forecast Details
* Category filtering

This page focuses on turning model predictions into understandable inventory insights.

---

## Page 2 — Model & Demand Analysis

The second page focuses on model performance and deeper demand analysis.

It includes:

* Model Performance
* Model Error Comparison
* Model Comparison Table
* Demand by Department
* Forecast by Category & Department
* Category, Store, Department and Model filters

The dashboard intentionally uses a limited number of pages to avoid repetitive charts and keep the analysis concise.

---

# 🛠️ Technologies Used

### Programming

* Python
* Pandas
* Polars
* NumPy

### Machine Learning

* Scikit-learn
* LightGBM
* XGBoost
* CatBoost

### Visualization & Analytics

* Matplotlib
* Seaborn
* Power BI

### Explainability

* SHAP

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

### Data Storage

* CSV
* Parquet

---

# 💡 Key Insights

The project demonstrates that:

* Machine learning models can provide useful demand forecasts from historical retail data.
* Tree-based models performed better than the basic Linear Regression baseline.
* LightGBM achieved the strongest overall performance based on R² and RMSE.
* Forecasted demand can be converted into simple inventory decisions.
* Category and department analysis helps identify areas with higher expected demand.
* Power BI can effectively communicate machine learning results to business users.

---

# 🎯 Business Value

The solution can help retailers:

* Identify products with higher expected demand
* Prioritize inventory replenishment
* Reduce unnecessary stock
* Understand category and department demand
* Compare forecasting models
* Turn machine learning predictions into actionable business recommendations

---

# ⚠️ Project Scope

The final forecasting workflow uses **CA_1 as the selected store**.

Therefore, the current project does not provide meaningful comparisons between multiple stores.

The reported model metrics reflect the specific dataset, feature engineering process, train/test strategy, and model configurations used in this project.

---

# 🔮 Future Improvements

Potential improvements include:

* Extend the pipeline to all stores
* Add more advanced lag and rolling-window features
* Perform hyperparameter tuning
* Use time-series cross-validation
* Forecast multiple future horizons
* Add prediction intervals
* Automate model retraining
* Deploy the forecasting pipeline
* Automate Power BI data refresh

---

# 👨‍💻 Author

**Nikesh Penala**

Data Analyst | Data Science & Machine Learning

**GitHub:** [https://github.com/Nikesh9646](https://github.com/Nikesh9646)

**LinkedIn:** [https://www.linkedin.com/in/nikesh-penala-a3576a324](https://www.linkedin.com/in/nikesh-penala-a3576a324)

---

## ⭐ Project Summary

```text
Data Preparation
      ↓
EDA
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Model Evaluation
      ↓
Demand Forecasting
      ↓
Inventory Optimization
      ↓
Power BI Dashboard
```

**An end-to-end demand forecasting solution combining machine learning with business intelligence.**
