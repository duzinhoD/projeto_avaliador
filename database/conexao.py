import sqlite3

def conectar():
    try:
        conexao = sqlite3.connect("database/padaria.db")
        return conexao
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
