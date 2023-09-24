import os
import pandas as pd
import streamlit as st

stock_datasets = os.listdir(r'C:\Users\piper\OneDrive\Desktop\web-app-dev\HackUMBCProject\stocks')
st.header("Dashboard")
ticker = st.text_input("Enter a stock ticker")
for dataset in stock_datasets:
    path = "C:\Users\piper\OneDrive\Desktop\web-app-dev\HackUMBCProject\stocks\\" + dataset
    df = pd.read_csv(dataset)
    dataset_ticker = dataset.split(".")[0]
    if dataset_ticker == ticker:
        st.write(df["Close"].head())