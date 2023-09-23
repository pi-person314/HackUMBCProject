import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.header('Movie')
title = st.text_input('Move title', 'Input movie title')
st.write('Your movie is: ', title)

st.dataframe(df)
movies = pd.read_csv('movies.csv')
print('We have ' + str(len(movies)) + ' movies')