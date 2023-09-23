import streamlit as st
import pandas as pd

text = st.text_input("Input name of movie")

movies = pd.read_csv("movies.csv")
movie_names = movies.name
trailers = movies.trailer
movieInput = text.split()
movieIndex = -1
for i in range(len(movies)):
    st.text(i)
    currentMovie = movie_names[i].split()
    rightMovie = True
    for j in movieInput:
        breakOut = False
        for k in currentMovie:
            if j not in k:
                rightMovie = False
    if not rightMovie:
        movieIndex = i
        break
st.text(movieIndex)