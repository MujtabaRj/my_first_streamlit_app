import streamlit as st

st.set_page_config(
    page_title='MLP',
    page_icon='📟'
)   

st.title('Main Page')
st.sidebar.success('Pages above')
st.header('Alan Turing',divider=True)
with st.sidebar:
    st.page_link("pages/analysis.py", label="Home", icon="🏠")

col1, col2 = st.columns(2)

with col1:
    st.image('download.jpg')

with col2:
    st.text("Born in London, Turing was raised in southern England. He graduated from King's College, Cambridge, and in 1938, earned a doctorate degree from Princeton University. During World War II, Turing worked for the Government Code and Cypher School at Bletchley Park, Britain's codebreaking centre that produced Ultra intelligence. He led Hut 8, the section responsible for German naval cryptanalysis. Turing devised techniques for speeding the breaking of German ciphers, including improvements to the pre-war Polish bomba method, an electromechanical machine that could find settings for the Enigma machine. ")

st.divider()