import os
import pandas as pd
import streamlit as st

stock_datasets = os.listdir("spstocks")
st.header("Dashboard")
ticker = st.text_input("Enter a stock ticker")
for dataset in stock_datasets:
    path = os.path.join("spstocks", dataset)
    df = pd.read_csv(path)
    dataset_ticker = dataset.split("_")[0]
    
    if dataset_ticker == ticker:
        st.write(df["close"].head())

        # Plotting the 'Close' column
        st.line_chart(df.set_index('date')["close"], use_container_width=True)
