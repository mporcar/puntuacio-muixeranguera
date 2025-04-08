import streamlit as st
import pandas as pd
import numpy as np 
st.title("Calculadora d'actuacions muixerangueres")
st.write("Aquesta és una calculadora de puntuacions d'actuacions muixerangueres que segueix la següent fórmula per calcular la puntuació de cada figura. " \
"En aquesta primera versió es consideraran 3 rondes amb figures sense multiplicitat i una ronda de pilars.")
st.latex(r'''
    Puntuació = a \cdot (Altura^q) \cdot \sqrt[p]{log(freq)} + \frac{Persones}{r} + 10\cdot FiguraDesplegada
    ''')

st.write("S'ha calculat la Frequüencia relativa de cada figura, a aquest numero se li ha aplicat el logaritme i se li ha canviat el signe, després aquest numero s'ha escalat entre 1 i 2 per tal que siga un multiplicador de raresa a una puntuació que creix per l'altura. A més a més el factor pinya es suma a una figura, ja que es vol premiar figures amb molta pinya pel que costa mobilitzar i coordinar a la pinya, també s'afegeixen 10 punts per figura desplegada")
df = pd.read_csv("Puntuacio.csv")


st.dataframe(df)

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
    np.arange(0,11)
)

pd4 = st.sidebar.selectbox(
    'Pilars de 4',
    np.arange(0,11)
)

pd5 = st.sidebar.selectbox(
    'Pilars de 5',
    np.arange(0,11)
)
st.write("Felicitats per l'Actuació")
st.dataframe(df.query("Figura in [@f1,@f2,@f3]"))

puntuació_total=df.query("Figura in [@f1,@f2,@f3]").Puntuació_total.sum()

st.write(f"La puntuació final ha sigut {puntuació_total}")