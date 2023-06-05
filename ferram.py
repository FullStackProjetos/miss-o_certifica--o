import tkinter as tk
import sqlite3


def cadastrar_ferramenta():
    cd_ferramenta = entry_codigo.get()
    des_ferramenta = entry_descricao.get()
    fb = entry_fabricante.get()
    vts = int(entry_voltagem.get())
    pt = float(entry_part_number.get())
    tm = float(entry_tamanho.get())
    un = float(entry_unidade.get())
    tpf = entry_tipo.get()
    mf = entry_material.get()

    conn = sqlite3.connect('cadastro_de_ferramentas.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_de_ferramenta (cd_ferramenta TEXT, des_ferramenta TEXT, fb TEXT, vts INTEGER, pt REAL, tm REAL, un REAL, tpf TEXT, mf TEXT)")
    cursor.execute("INSERT INTO cadastro_de_ferramenta VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (cd_ferramenta, des_ferramenta, fb, vts, pt, tm, un, tpf, mf))

    conn.commit()
    conn.close()

    # Limpar os campos de entrada após o cadastro
    entry_codigo.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_fabricante.delete(0, tk.END)
    entry_voltagem.delete(0, tk.END)
    entry_part_number.delete(0, tk.END)
    entry_tamanho.delete(0, tk.END)
    entry_unidade.delete(0, tk.END)
    entry_tipo.delete(0, tk.END)
    entry_material.delete(0, tk.END)


janela = tk.Tk()
janela.title('Cadastro de Ferramentas')
janela.geometry('400x700')

label_codigo = tk.Label(janela, text='Código de Ferramenta:')
label_codigo.pack()
entry_codigo = tk.Entry(janela, width=30)
entry_codigo.pack()

label_descricao = tk.Label(janela, text='Descrição de Ferramenta:')
label_descricao.pack()
entry_descricao = tk.Entry(janela, width=30)
entry_descricao.pack()

label_fabricante = tk.Label(janela, text='Fabricante:')
label_fabricante.pack()
entry_fabricante = tk.Entry(janela, width=30)
entry_fabricante.pack()

label_voltagem = tk.Label(janela, text='Voltagem de Uso:')
label_voltagem.pack()
entry_voltagem = tk.Entry(janela, width=30)
entry_voltagem.pack()

label_part_number = tk.Label(janela, text='Part Number:')
label_part_number.pack()
entry_part_number = tk.Entry(janela, width=30)
entry_part_number.pack()

label_tamanho = tk.Label(janela, text='Tamanho da Ferramenta:')
label_tamanho.pack()
entry_tamanho = tk.Entry(janela, width=30)
entry_tamanho.pack()

label_unidade = tk.Label(janela, text='Unidade de Medida:')
label_unidade.pack()
entry_unidade = tk.Entry(janela, width=30)
entry_unidade.pack()

label_tipo = tk.Label(janela, text='Tipo de Ferramenta:')
label_tipo.pack()
entry_tipo = tk.Entry(janela, width=30)
entry_tipo.pack()

label_material = tk.Label(janela, text='Material da Ferramenta:')
label_material.pack()
entry_material = tk.Entry(janela, width=30)
entry_material.pack()

button_cadastrar = tk.Button(janela, text='Cadastrar', command=cadastrar_ferramenta)
button_cadastrar.pack()

janela.mainloop()