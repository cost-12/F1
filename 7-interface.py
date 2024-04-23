import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# conectando bd
conexao = sqlite3.connect('F1.db')
cursor = conexao.cursor()

st.title('Fórmula 1')

# cadastro
st.header('Cadastro de Equipe')
equipe = st.text_input('Nome da Equipe')
chassi = st.number_input('Chassi')
aerodinamica = st.number_input('Aerodinâmica')
motor = st.number_input('Motor')
durabilidade = st.number_input('Durabilidade')

if st.button('Cadastrar'):
    cursor.execute(
        """
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES (?, ?, ?, ?, ?)
        """,
        (equipe, chassi, aerodinamica, motor, durabilidade)
    )
    conexao.commit()
    st.success('Equipe cadastrada com sucesso!')

st.header('Lista de Equipes')
cursor.execute("SELECT * FROM F1")
equipes = cursor.fetchall()

# Criando um DataFrame com os dados
df = pd.DataFrame(equipes, columns=['Equipe', 'Chassi', 'Aerodinâmica', 'Motor', 'Durabilidade'])

# Calculo desempenho
df['Desempenho Geral'] = df[['Chassi', 'Aerodinâmica', 'Motor', 'Durabilidade']].sum(axis=1)

df = df.sort_values(by='Desempenho Geral', ascending=False)

# Exibindo a tabela
st.dataframe(df)

# gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['Equipe'], df['Desempenho Geral'])
plt.xlabel('Equipes')
plt.ylabel('Desempenho Geral')
plt.title('Ranking de Desempenho Geral das Equipes')
plt.xticks(rotation=45)
st.pyplot(plt)


conexao.close()
