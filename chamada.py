#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from datetime import datetime
import subprocess

leitorRfid = SimpleMFRC522()
ids_lidos = set()
data_atual = datetime.now().strftime("%d-%m-%Y")
nome_arquivo = f"rfid_{data_atual}.txt"
alunos_cadastrados = {}

# Função para ler o arquivo de alunos cadastrados
def ler_arquivo_alunos():
    alunos_cadastrados.clear()
    with open("alunos.txt", "r") as f:
        for line in f:
            id_aluno, matricula, nome = line.strip().split(",")
            alunos_cadastrados[int(id_aluno)] = (matricula, nome)

# Lê o arquivo de alunos cadastrados inicialmente
ler_arquivo_alunos()

try:
    while True:
        print("Aproxime a carteirinha...")
        id, text = leitorRfid.read()

        # Verifica se o aluno está cadastrado
        if id not in alunos_cadastrados:
            print("Aluno não cadastrado")

            cadastrar_aluno = input("Deseja cadastrar o aluno agora? (s/n) ")
            if cadastrar_aluno.lower() == "s":
                # Abre o programa de cadastro
                GPIO.cleanup()
                subprocess.run(["python3", "cadastro.py"])

                # Pausar a execução do código
                #GPIO.cleanup()
                continuar = input("Deseja continuar a chamada? (s/n) ")
                if continuar.lower() != "s":
                    break

                # Releitura do arquivo de alunos
                ler_arquivo_alunos()
            else:
                continue

        if id not in ids_lidos:
            ids_lidos.add(id)
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            matricula, nome = alunos_cadastrados[id]
            with open(nome_arquivo, "a") as f:
                f.write(f"{matricula} - {nome} - {data_hora}\n")
            print(f"Informações do aluno {nome} salvas no arquivo '{nome_arquivo}'")
        else:
            print(f"O cartão com ID {id} já foi lido anteriormente.")

        # Verifica se mudou o dia e atualiza o nome do arquivo
        nova_data_atual = datetime.now().strftime("%d-%m-%Y")
        if nova_data_atual != data_atual:
            data_atual = nova_data_atual
            nome_arquivo = f"rfid_{data_atual}.txt"
            ids_lidos.clear()
            print(f"Novo dia começou, criando arquivo '{nome_arquivo}'")
except KeyboardInterrupt:
    GPIO.cleanup()