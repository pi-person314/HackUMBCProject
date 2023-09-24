import os
import pandas as pd
import streamlit as st

stock_datasets = os.listdir("stocks")
st.header("Dashboard")
ticker = st.text_input("Enter a stock ticker")
for dataset in stock_datasets:
    path = os.path.join("stocks", dataset)
    df = pd.read_csv(path)
    dataset_ticker = dataset.split(".")[0]
    
    if dataset_ticker == ticker:
        st.write(df["Close"].head())

        # Plotting the 'Close' column
        st.line_chart(df.set_index('Date')["Close"], use_container_width=True)
