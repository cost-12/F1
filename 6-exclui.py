import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('F1.db')
cursor = conexao.cursor()

# 2-Exclusão
Equipe = ('Ferrari',)
cursor.execute(
    """
    DELETE FROM F1
    WHERE Equipe = ?
    """,
    Equipe
)
conexao.commit()

conexao.close()