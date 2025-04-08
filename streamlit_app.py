import streamlit as st
import pandas as pd
import numpy as np 
st.write("Aquesta és una calculadora de puntuacions d'actuacions muixerangueres")

df = pd.read_csv("Puntuacio.csv")

add_slider = st.sidebar.slider(
    'Select a range of values',
    3, 6, (3, 6)
)

st.write(add_slider)
menor=add_slider[0]
major=add_slider[1]
st.dataframe(df.query("Altura >= @menor and Altura <= @major"))

f1 = st.sidebar.selectbox(
    'Primera Figura',
    df.Figura
)

f2 = st.sidebar.selectbox(
    'Segona Figura',
    df.Figura
)

f3 = st.sidebar.selectbox(
    'Tercera Figura',
    df.Figura
)

pd3 = st.sidebar.selectbox(
    'Pilars de 3',
    np.arange(1,11)
)

pd4 = st.sidebar.selectbox(
    'Pilars de 4',
    np.arange(1,11)
)

pd5 = st.sidebar.selectbox(
    'Pilars de 5',
    np.arange(1,11)
)
st.write("Felicitats per l'Actuació")
st.dataframe(df.query("Figura in [@f1,@f2,@f3]"))

puntuació_total=df.query("Figura in [@f1,@f2,@f3]").Puntuació_total.sum()

st.write(f"La puntuació final ha sigut {puntuació_total}")