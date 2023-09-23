import streamlit as st
import pandas as pd

st.markdown('<link rel="stylesheet" href="assets/styles.css">', unsafe_allow_html=True)


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.dataframe(df)