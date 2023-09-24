import os
import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.graph_objs as go

class InvalidTickerError(Exception):
    pass

def load_stock_data(ticker):
    stock_datasets = os.listdir("spstocks")
    for dataset in stock_datasets:
        if dataset.startswith(ticker):
            path = os.path.join("spstocks", dataset)
            df = pd.read_csv(path)
            return df
    return None

def get_data(ticker, start_date, end_date):
    df = load_stock_data(ticker)
    if df is None:
        raise InvalidTickerError(f"No data found for ticker: {ticker}")
    if 'Name' not in df.columns:
        st.write(f"Columns in the dataset are: {df.columns}")
        raise InvalidTickerError(f"Invalid data format for ticker: {ticker}")
    return df[df['Name'] == ticker]

def generate_predictions(data):
    # Placeholder - replace with your AI model prediction code
    return data['close'].values  # Assuming 'close' is the column you want to predict

def display_stock_info(df):
    total_length = len(df)
    split_index = total_length // 2
    
    known_data = df.iloc[:split_index]
    prediction_data = df.iloc[split_index:]
    
    predicted_values = generate_predictions(prediction_data)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=known_data['date'], y=known_data['close'], mode='lines', name='Known Data'))
    fig.add_trace(go.Scatter(x=prediction_data['date'], y=predicted_values, mode='lines', name='AI Predictions'))
    
    st.plotly_chart(fig)

def apply_styles():
    hide_st_style = """
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def display_intro():
    pass  # Placeholder for your intro display function

def main():
    st.set_page_config(page_title="Predictbay", page_icon=":chart_with_upwards_trend:", layout="wide")
    apply_styles()

    st.title(':chart_with_upwards_trend: Predictbay')
    display_intro()

    st.subheader('- Closing Price')
    user_input = st.text_input('Enter a Valid stock Ticker')
    if user_input != "":
        try:
            df = get_data(user_input, '2010-01-01', datetime.now())
            display_stock_info(df)
        except InvalidTickerError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
