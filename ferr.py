import tkinter as tk
import sqlite3


def cadastrar():
    cpf = int(entry_cpf.get())
    nome = entry_nome.get()
    telefone = int(entry_telefone.get())
    turno = entry_turno.get()
    equipe = entry_equipe.get()

    conn = sqlite3.connect('cadastro_de_funcionario.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_funcionario (cpf INTEGER, nome TEXT, telefone INTEGER, turno TEXT, equipe TEXT)")
    cursor.execute("INSERT INTO cadastro_funcionario VALUES (?, ?, ?, ?, ?)", (cpf, nome, telefone, turno, equipe))

    conn.commit()
    conn.close()

    # Limpar os campos de entrada após o cadastro
    entry_cpf.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_turno.delete(0, tk.END)
    entry_equipe.delete(0, tk.END)


janela = tk.Tk()
janela.title('Cadastro de Funcionários')
janela.geometry('450x450')

label_cpf = tk.Label(janela, text='CPF:')
label_cpf.pack()
entry_cpf = tk.Entry(janela, width=30)
entry_cpf.pack()

label_nome = tk.Label(janela, text='Nome:')
label_nome.pack()
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

label_telefone = tk.Label(janela, text='Telefone:')
label_telefone.pack()
entry_telefone = tk.Entry(janela, width=30)
entry_telefone.pack()

label_turno = tk.Label(janela, text='Turno de Trabalho:')
label_turno.pack()
entry_turno = tk.Entry(janela, width=30)
entry_turno.pack()

label_equipe = tk.Label(janela, text='Nome da Equipe:')
label_equipe.pack()
entry_equipe = tk.Entry(janela, width=30)
entry_equipe.pack()

botao_cadastrar = tk.Button(janela, text='Cadastrar', command=cadastrar)
botao_cadastrar.pack()

janela.mainloop()