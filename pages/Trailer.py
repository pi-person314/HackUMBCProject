import streamlit as st
import pandas as pd

st.header('Trailers')
title = st.text_input('Move title', 'Input movie title')
st.write('Your movie is: ', title)

video_file = open('"C:\Users\victo\Downloads\aacdaebc-d2c5-41dc-bb38-c481f55b235b.mp4"', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)