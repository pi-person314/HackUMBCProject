import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.title(':scales: Compare Stocks')

stock_datasets = os.listdir("spstocks")

ticker = st.text_input("Enter a stock ticker in the S&P 500")
ticker2 = st.text_input("Enter another stock ticker in the S&P 500")
col1, col2 = st.columns(2)



for dataset in stock_datasets:
    path = os.path.join("spstocks", dataset)
    df = pd.read_csv(path)
    dataset_ticker = dataset.split("_")[0]
    if dataset_ticker == ticker:
        with col1:
            tab1, tab2, tab3 = st.tabs(["Closing", "Volume", "Candle"])
            with tab1:
                st.subheader(f"Closing Prices for {ticker}")
                st.line_chart(df.set_index('date')["close"], use_container_width=True)

            with tab2:
                st.subheader(f"Volume Distribution for {ticker}")
                st.bar_chart(df.set_index('date')["volume"], use_container_width=True)

            with tab3:
                st.subheader(f"Candlestick Chart for {ticker}")
                fig = go.Figure(data=[go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
                st.plotly_chart(fig, use_container_width=True)

    if dataset_ticker == ticker2:
        with col2:
            tab1, tab2, tab3 = st.tabs(["Closing", "Volume", "Candle"])
            with tab1:
                st.subheader(f"Closing Prices for {ticker2}")
                st.line_chart(df.set_index('date')["close"], use_container_width=True)

            with tab2:
                st.subheader(f"Volume Distribution for {ticker2}")
                st.bar_chart(df.set_index('date')["volume"], use_container_width=True)

            with tab3:
                st.subheader(f"Candlestick Chart for {ticker2}")
                fig = go.Figure(data=[go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
                st.plotly_chart(fig, use_container_width=True)
            break