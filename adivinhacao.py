print("***********************************")
print("Bem vindo no jogo de adivinhação!")
print("***********************************\n")

numero_secreto = 23
total_de_tentativas_str = input("Qual dificuldade você deseja? \n1- Fácil \n2- Médio \n3- Difícil \n \nDificuldade: ")
if(total_de_tentativas_str == "Fácil"):
    total_de_tentativas = 10
elif(total_de_tentativas_str == "Médio"):
    total_de_tentativas = 7
elif(total_de_tentativas_str == "Difícil"):
    total_de_tentativas = 5
else:
    print("Digite uma dificuldade válida")

print("\nVocê tem ", total_de_tentativas, " tentativas \n")
tentativas = 1

while(tentativas <= total_de_tentativas):
    print("Tentativa: {} de {}".format(tentativas, total_de_tentativas))
    chute_str = input("Digite sua tentativa: ")
    chute = int(chute_str)

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
print("Fim do jogo!")