import streamlit as st
import dados

st.title("Fórmula 1")

def insere_dados(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        '''
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES (?, ?, ?, ?, ?)
        ''',(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
    )
    conexao.commit()
    conexao.close()

# Função para inserir dados de exemplo (opcional)
def inserir_dados_exemplo():
    insere_dados('Audi F1 TEAM', '9.0', '7.0', '10', '9.0')

# Executar a inserção de dados de exemplo apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    inserir_dados_exemplo()
