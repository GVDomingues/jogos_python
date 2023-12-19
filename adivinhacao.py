def jogar():
    print("***********************************")
    print("*Bem vindo no jogo de adivinhação!*")
    print("***********************************\n")

    import random
    numero_secreto = random.randrange(1, 100)
    pontuacao = 1000

    while True: #definir quantidade de tentativas
        total_de_tentativas_str = input("Qual dificuldade você deseja? \n1- Fácil \n2- Médio \n3- Difícil \n \nDificuldade: ")
        if total_de_tentativas_str.lower() in ["1", "facil", "fácil"]:
            total_de_tentativas = 10
            break
        if total_de_tentativas_str.lower() in ["2", "medio", "médio"]:
            total_de_tentativas = 7
            break
        if total_de_tentativas_str.lower() in ["3", "dificil", "difícil"]:
            total_de_tentativas = 5
            break
        else:
            print("Digite uma dificuldade válida\n")

    erro = int(pontuacao/total_de_tentativas)

    print("\nVocê tem ", total_de_tentativas, " tentativas")
    tentativas = 1

    while(tentativas <= total_de_tentativas):
        print("\nTentativa: {} de {} \nVocê tem {} pontos".format(tentativas, total_de_tentativas, pontuacao))
        chute_str = input("\n Digite um número de 1 a 99: ")
        chute = int(chute_str)

        if(chute < 1) or (chute > 99):
            print("Digite um número válido")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("")
            print("\nVocê acertou!")
            break
        else:
            if(maior):
                print("Você errou! O número digitado é maior do que o número secreto")
            elif(menor):
                print("Você errou! O número digitado é menor do que o número secreto")

        tentativas = tentativas + 1
        pontuacao = int(pontuacao-erro)
    print(f"O número secreto era {numero_secreto}")
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()