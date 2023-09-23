import streamlit as st
import pandas as pd

#Styling
primaryColor="#FFFFFF"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#FFFFFF"
textColor="#FFFFFF"
font="sans serif"

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df