import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers='UBER', period='5d', interval='5m')
data