#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def aluno_presente(id):
    try:
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if int(dados[0]) == id:
                    return True
    except FileNotFoundError:
        return False
    return False

def main():
    reader = SimpleMFRC522()

    while True:
        # Solicitar que o cartão seja aproximado
        print("Aproxime a carteirinha para leitura...")
        id, _ = reader.read()

        # Verificar se o aluno já está presente no arquivo
        if aluno_presente(id):
            print("Aluno já presente no arquivo.")
        else:
            # Perguntar o nome e a matrícula do aluno
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")

            # Armazenar os dados em um arquivo de texto
            with open("alunos.txt", "a") as arquivo:
                arquivo.write(f"{id},{matricula},{nome}\n")
                print("Dados do aluno armazenados com sucesso!")

        # Perguntar se deseja fazer uma nova verificação
        resposta = input("Deseja cadastrar mais outro aluno? (S/N): ")
        if resposta.lower() != "s":
            break

if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()