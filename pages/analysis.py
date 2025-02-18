import streamlit as st
import pandas as pd

st.header('Analysis',divider=True)
df = pd.read_csv('Automobile.csv')
st.dataframe(df)

st.bar_chart(df['company'])

st.line_chart(df['length'])