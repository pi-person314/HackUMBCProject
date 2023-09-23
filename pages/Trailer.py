import streamlit as st
import pandas as pd

text = st.text_input("Input name of movie")

if text != "":
    movies = pd.read_csv("movies.csv")
    movie_names = movies["name"]
    trailers = movies["trailer"]
    movie_trailers = ["no trailer available" if trailer is None else trailer for trailer in trailers]

    movieIndex = -1

    for i in range(len(movies)):
        movieFound = False
        if text in movie_names[i]:
            movieIndex = i
            movieFound = True
        if movieFound:
            break
    if movieIndex == -1:
        st.text("no movies found")
    else:
        st.text(movie_names[movieIndex])
        st.text(movie_trailers[movieIndex])