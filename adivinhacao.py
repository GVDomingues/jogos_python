print("***********************************")
print("Bem vindo no jogo de adivinhação!")
print("***********************************")
print("")

numero_secreto = 23
chute_str = input("Digite sua tentativa: ")
chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O número digitado é maior do que o número secreto")
    elif(menor):
        print("Você errou! O número digitado é menor do que o número secreto")

print("Fim do jogo!")