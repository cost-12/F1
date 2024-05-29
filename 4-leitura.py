import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('F1.db')
cursor = conexao.cursor()

# 2 - Leitura de Dados
equipe = 'Renault'
cursor.execute(
    "SELECT Durabilidade FROM F1 WHERE Equipe = ?",
    (equipe,)
)
Durabilidade = cursor.fetchone()
print(Durabilidade)