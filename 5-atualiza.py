import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('F1.db')
cursor = conexao.cursor()

# 2-Atualização
nova_equipe = "Mercedes F1 TEAM"
antiga_equipe = "Mercedes-Benz"
cursor.execute(
    """
    UPDATE F1 SET Equipe = ?
    WHERE Equipe = ?
    """,
    (nova_equipe, antiga_equipe)
)
conexao.commit()