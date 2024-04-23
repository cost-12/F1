import streamlit as st
import dados

st.title("F1")

Equipe = st.text_input('Equipe')
Chassi = st.number_input()
Aerodinâmica = st.number_input()
Motor = st.number_input()
Durabilidade = st.number_input()

if st.button('Adcionar'):
    dados.insere_dados(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
    
