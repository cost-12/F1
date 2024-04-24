import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('F1.db')
cursor = conexao.cursor()

# 2-Atualização
nova_equipe = "Porsche MARTINI"
antiga_equipe = "Porsches MARTINI"
cursor.execute(
    """
    UPDATE F1 SET Equipe = ?
    WHERE Equipe = ?
    """,
    (nova_equipe, antiga_equipe)
)
conexao.commit()