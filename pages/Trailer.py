import streamlit as st
import pandas as pd

text = st.text_input("Input name of movie")

if text == "Rise of Skywalker":
    st.header('Trailer: Rise of Skywalker')
    st.video('https://youtu.be/8Qn_spdM5Zg?si=k3hSMV_Suzh8MmL_')