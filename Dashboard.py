import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt



stock_datasets = os.listdir("spstocks")
st.header("Search for Stocks")
ticker = st.text_input("Enter a stock ticker in the S&P 500")
ticker2 = st.text_input("Enter another stock ticker in the S&P 500")

for dataset in stock_datasets:
    path = os.path.join("spstocks", dataset)
    df = pd.read_csv(path)
    dataset_ticker = dataset.split("_")[0]

    path2 = os.path.join("spstocks", dataset)
    df2 = pd.read_csv(path2)
    dataset_ticker2 = dataset.split("_")[0]
    
    if dataset_ticker == ticker:
        st.subheader(f"Closing Prices for {ticker}")
        st.line_chart(df.set_index('date')["close"], use_container_width=True)
        st.subheader(f"Volume Distribution for {ticker}")
        st.bar_chart(df.set_index('date')["volume"], use_container_width=True)
        st.subheader(f"Candlestick Chart for {ticker}")
        fig = go.Figure(data=[go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
        st.plotly_chart(fig, use_container_width=True)

    if dataset_ticker2 == ticker2:
        st.subheader(f"Closing Prices for {ticker2}")
        st.line_chart(df2.set_index('date')["close"], use_container_width=True)
        st.subheader(f"Volume Distribution for {ticker2}")
        st.bar_chart(df2.set_index('date')["volume"], use_container_width=True)
        st.subheader(f"Candlestick Chart for {ticker2}")
        fig = go.Figure(data=[go.Candlestick(x=df2['date'], open=df2['open'], high=df2['high'], low=df2['low'], close=df2['close'])])
        st.plotly_chart(fig, use_container_width=True)
        break