import streamlit as st
import pandas as pd
st.set_page_config(page_title="Enterprise Demand Forecasting")

st.title("Enterprise Demand Forecasting Dashboard")
st.write("Retail demand forecasting and inventory optimization using LightGBM.")

forecast = pd.read_csv("../reports/forecast_results.csv")

inventory = pd.read_csv("../reports/inventory_recommendations.csv")

product = st.text_input("Search Product")

if product:
    st.dataframe(
        inventory[
            inventory["item_id"].str.contains(
                product,
                case=False
            )
        ]
    ) 
    
st.sidebar.header("Filters")

recommendation = st.sidebar.selectbox(
    "Recommendation",
    ["All"] + list(inventory["Recommendation"].unique())
)

if recommendation != "All":
    inventory = inventory[
        inventory["Recommendation"] == recommendation
    ]
        
st.metric("Total Products", len(forecast))

st.metric(
    "Average Forecast",
    round(forecast["forecast_sales"].mean(), 2)
)

st.metric(
    "High Demand Items",
    len(forecast[forecast["forecast_sales"] >= 5])
)    

st.header("Forecasted Sales")

st.dataframe(forecast)

st.header("Inventory Recommendations")

st.dataframe(inventory)

st.header("Recommendation Distribution")

st.bar_chart(
    inventory["Recommendation"].value_counts()
)


