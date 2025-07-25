import tkinter as tk

def abrir_menu():
    janela = tk.Tk()
    janela.title("Menu Principal")
    janela.geometry("400x200")

    tk.Label(janela, text="Bem-vindo ao Sistema da Padaria!").pack(pady=20)
    tk.Button(janela, text="Sair", command=janela.destroy).pack(pady=10)

    janela.mainloop()
