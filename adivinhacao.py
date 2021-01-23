import random
import re

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    total_escolhido = int(input("Digite o tamanho de números para advinhação: "))
    numero_secreto = random.randrange(1, total_escolhido+1)
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 0

    nivel = int(input("Qual nível de dificuldade?\n"
          "(1) Fácil (2) Médio (3) Difícil: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e {}: ".format(total_escolhido))
        print("Você digitou ", chute_str)

        if(chute < 1 or chute > total_escolhido):
            print("Você deve digitar um número entre 1 e {}: ".format(total_escolhido))
            continue

        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        pontos = nivel * (1000 / rodada)

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
