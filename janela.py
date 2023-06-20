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
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            label["text"] += line

    label.pack()


# Função para executar o arquivo chamada.py em um novo terminal
def run_chamada():
    subprocess.Popen(['x-terminal-emulator', '-e', 'python3 chamada.py'])

def run_cadastro():
    subprocess.Popen(['x-terminal-emulator', '-e', 'python3 cadastro.py'])


# Cria a janela principal
root = tk.Tk()
root.title("Controle de presença")
root.geometry("400x300")  # Definir as dimensões da janela principal (largura x altura)

# Definir cores
button_bg = "#4369D4"  # Azul
button_fg = "white"  # Branco

frame = tk.Frame(root)
frame.pack(pady=10)


# Botão para visualizar alunos presentes
btn_visualizar = tk.Button(frame, text="Ver alunos presentes", command=open_file,
                           bg=button_bg, fg=button_fg)
btn_visualizar.pack(side=tk.LEFT, padx=10)  # Adicionar preenchimento horizontal

btn_chamada = tk.Button(root, text="Chamada", command=run_chamada,
                        bg=button_bg, fg=button_fg)
btn_chamada.pack(pady=5)

btn_cadastrar = tk.Button(root, text="Cadastrar aluno", command=run_cadastro,
                          bg=button_bg, fg=button_fg)
btn_cadastrar.pack(pady=5)

root.mainloop()
