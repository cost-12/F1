import sqlite3

# Conecta bd
def conecta_bd():
    conexao = sqlite3.connect('F1.db')
    return conexao

# Insere dados
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

insere_dados('Audi F1 TEAM', '9.0', '7.0', '10', '9.0')
