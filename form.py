import streamlit as st
import dados

st.title("Fórmula 1")

Equipe = st.text_input('Nome da equipe:')
Chassi = st.slider('Chassi', min_value=0.0, max_value=10.0)
Aerodinâmica = st.slider('Aerodinâmica', min_value=0.0, max_value=10.0)
Motor = st.slider('Motor', min_value=0.0, max_value=10.0)
Durabilidade = st.slider('Durabilidade', min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    dados.insere_dados(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
    st.success("Sucesso")
