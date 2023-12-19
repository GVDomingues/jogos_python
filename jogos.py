import adivinhacao
import forca

def escolher_jogo():
    print("***********************************")
    print("*********Escolha seu jogo!*********")
    print("***********************************\n")

    while True:
        jogo = input("Qual jogo você quer jogar?\n1- Adivinhação\n2- Forca\n\n")
        if jogo.lower() in ["1", "adivinhacao", "adivinhaçao", "adivinhacão", "adivinhação"]:
            print("\n\nJogando adivinhação")
            adivinhacao.jogar()
            break
        elif jogo.lower() in ["2", "forca"]:
            print("\n\nJogando forca")
            forca.jogar()
            break
        else:
            print("Escolha uma opção válida\n")

if(__name__ == "__main__"):
    escolher_jogo()