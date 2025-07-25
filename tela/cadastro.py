import tkinter as tk
from controller.usuario_controller import cadastrar_usuario

def abrir_tela_cadastro():
    janela = tk.Toplevel()
    janela.title("Cadastro")
    janela.geometry("300x200")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Email:").pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Label(janela, text="Senha:").pack()
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        if cadastrar_usuario(nome, email, senha):
            tk.Label(janela, text="Usuário cadastrado com sucesso!", fg="green").pack()
        else:
            tk.Label(janela, text="Erro ao cadastrar!", fg="red").pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)
