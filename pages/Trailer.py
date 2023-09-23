import streamlit as st
import pandas as pd

text = st.text_input("Input name of movie", "Movie Name")

if text != "Movie Name":
    movies = pd.read_csv("movies.csv")
    movie_names = movies.name
    trailers = movies.trailer
    movieIndex = -1

    for i in range(len(movies)):
        movieFound = False
        if text in movie_names[i]:
            movieIndex = i
            movieFound = True
        if movieFound:
            break
    st.text(movie_names[movieIndex])

#movies = pd.read_csv('')
#df = pd.DataFrame(movies)
#df.dropna(
   #axis=0,
   #how='any',
   #thresh=None,
   #subset=None,
   #inplace=False
#)
#df.dropna(np.nan)

