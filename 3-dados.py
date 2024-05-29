import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('F1.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES ('Mercedes', 9.0, 8.7, 9.9, 9.2)
    """
)

cursor.execute(
    """
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES ('Ferrari', 8.3, 8.9, 10, 8.2)
    """
)

cursor.execute(
    """
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES ('Red Bull', 9.4, 9.8, 7.5, 8.1)
    """
)

cursor.execute(
    """
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES ('McLaren', 7.5, 8.2, 7.8, 8.8)
    """
)

cursor.execute(
    """
        INSERT INTO F1(Equipe, Chassi, Aerodinâmica, Motor, Durabilidade)
        VALUES ('Renault', 8.0, 7.5, 7.8, 9.6)
    """
)

conexao.commit()
conexao.close()