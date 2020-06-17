import forca
import adivinhacao

print("*********************************")
print("********Escolha seu jogo!******")
print("*********************************")

print("(1) Forca (2) Adivinhação!")
jogo = int(input("Qual jogo você quer Jogar? "))

if (jogo == 1):
    print("Jojando forca")
    forca.jogar()
else:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
 