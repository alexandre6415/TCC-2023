#!/usr/bin/env python

import tkinter as tk
from tkinter import filedialog
import subprocess

# Função para abrir um arquivo de texto
def open_file():
    # Abre a caixa de diálogo para selecionar o arquivo de texto
    file_path = filedialog.askopenfilename()

    # Cria um rótulo para exibir as linhas do arquivo de texto
    label = tk.Label(root, text="")

    # Lê o arquivo de texto e adiciona cada linha ao rótulo
    with open(file_path, "r") as file:
        for line in file:
            label["text"] += line

    # Adiciona o rótulo à janela principal
    label.pack()

# Função para executar o arquivo chamada.py em um novo terminal
def run_chamada():
    subprocess.Popen(['x-terminal-emulator', '-e', 'python3 chamada.py'])

# Função para executar o arquivo cadastro.py em um novo terminal
def run_cadastro():
    subprocess.Popen(['x-terminal-emulator', '-e', 'python3 cadastro.py'])

# Cria a janela principal
root = tk.Tk()

# Botão para visualizar alunos presentes
btn_visualizar = tk.Button(root, text="Visualizar alunos presentes", command=open_file)
btn_visualizar.pack()

# Botão para executar o arquivo chamada.py em um novo terminal
btn_chamada = tk.Button(root, text="Chamada", command=run_chamada)
btn_chamada.pack()

# Botão para executar o arquivo cadastro.py em um novo terminal
btn_cadastrar = tk.Button(root, text="Cadastrar aluno", command=run_cadastro)
btn_cadastrar.pack()

# Inicia o loop da interface gráfica
root.mainloop()