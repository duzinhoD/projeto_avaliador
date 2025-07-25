from database.conexao import conectar

def cadastrar_usuario(nome, email, senha):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        """, (nome, email, senha))
        conexao.commit()
        return True
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
        return False
    finally:
        conexao.close()

def fazer_login(email, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM usuarios WHERE email = ? AND senha = ?
    """, (email, senha))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario
