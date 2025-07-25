import tkinter as tk
from controller.usuario_controller import fazer_login
from tela.menu import abrir_menu

def abrir_login():
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry("300x200")

    tk.Label(janela, text="Email:").pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Label(janela, text="Senha:").pack()
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    def logar():
        email = entry_email.get()
        senha = entry_senha.get()
        usuario = fazer_login(email, senha)
        if usuario:
            janela.destroy()
            abrir_menu()
        else:
            tk.Label(janela, text="Login inválido!", fg="red").pack()

    tk.Button(janela, text="Entrar", command=logar).pack(pady=10)

    from tela.cadastro import abrir_tela_cadastro
    tk.Button(janela, text="Cadastrar", command=abrir_tela_cadastro).pack()

    janela.mainloop()
