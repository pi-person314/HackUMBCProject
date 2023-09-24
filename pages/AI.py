import os
import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.graph_objs as go
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
import numpy as np

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

def generate_predictions(data):
    dataset = data['close'].values
    dataset = dataset.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    
    train_length = int(len(scaled_data) * 0.8)
    train_data = scaled_data[:train_length]
    
    x_train, y_train = [], []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=2, batch_size=32)

    total_length = len(scaled_data)
    x_test = []
    for i in range(train_length - 60, total_length - 60):
        x_test.append(scaled_data[i:i+60, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    
    return predictions

def display_stock_info(df):
    df_until_2018 = df[df['date'] <= '2018-12-31']
    known_data = df_until_2018.iloc[:-len(df_until_2018)//2]
    ai_prediction_data = df_until_2018.iloc[-len(df_until_2018)//2:]
    
    predicted_values = generate_predictions(known_data)

    # Plotting AI predictions along with the original first half
    fig_predictions = go.Figure()
    fig_predictions.add_trace(go.Scatter(x=known_data['date'], y=known_data['close'], mode='lines', name='Original Data'))
    fig_predictions.add_trace(go.Scatter(x=ai_prediction_data['date'], y=predicted_values.reshape(-1), mode='lines', name='AI Predictions'))
    st.plotly_chart(fig_predictions, use_container_width=True)
    
    # Plotting original data and AI predictions together
    fig_original = go.Figure()
    fig_original.add_trace(go.Scatter(x=df_until_2018['date'], y=df_until_2018['close'], mode='lines', name='Full Original Data'))
    st.plotly_chart(fig_original, use_container_width=True)

def display_intro():
    pass  # Placeholder for your intro display function

def main():
    st.title(':chart_with_upwards_trend: Predictbay')
    display_intro()

    st.subheader('- Closing Price')
    user_input = st.text_input('Enter a Valid stock Ticker')
    if (user_input != ""):
        try:
            df = load_stock_data(user_input)
            if df is None:
                raise InvalidTickerError(f"No data found for ticker: {user_input}")
            display_stock_info(df)
        except InvalidTickerError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
