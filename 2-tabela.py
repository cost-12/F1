import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('F1.db')

cursor = conexao.cursor()

# 2-Criação da Tabela
cursor.execute(
    """
        CREATE TABLE F1(
            Equipe VARCHAR(255) NOT NULL PRIMARY KEY,  
            Chassi DOUBLE NOT NULL,
            Aerodinâmica DOUBLE NOT NULL,
            Motor DOUBLE NOT NULL,
            Durabilidade DOUBLE NOT NULL
        );
    """
)
# 3- Fecha conexão
conexao.close()
print("Tabela foi criada")