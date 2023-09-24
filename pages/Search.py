import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt

stock_datasets = os.listdir("spstocks")
st.header("Search for Stocks")
ticker = st.text_input("Enter a stock ticker")

for dataset in stock_datasets:
    path = os.path.join("spstocks", dataset)
    df = pd.read_csv(path)
    dataset_ticker = dataset.split("_")[0]
    
    if dataset_ticker == ticker:
        st.write(df["close"].head())

        # 1. Line chart for Closing Prices
        st.subheader(f"Closing Prices for {ticker}")
        st.line_chart(df.set_index('date')["close"], use_container_width=True)
        
        # 2. Histogram for Volume Distribution
        st.subheader(f"Volume Distribution for {ticker}")
        st.bar_chart(df.set_index('date')["volume"], use_container_width=True)

        # 3. Candlestick plot
        st.subheader(f"Candlestick Chart for {ticker}")
        fig = go.Figure(data=[go.Candlestick(x=df['date'],
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])
        st.plotly_chart(fig, use_container_width=True)

        break