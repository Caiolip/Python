import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    totalp = 100

    print("Escolha um nivel!")
    print("(1) Fácil (2) Médio (3) Díficil")
    nivel = int(input("Digite o numero referente ao nivel: "))

    if(nivel == 1):
        tentativas = 20
        totalp = 80
    if (nivel == 2):
        tentativas = 10
        totalp = 90
    if (nivel == 3):
        tentativas = 5
        totalp = 100

    for rodada in range(1, tentativas + 1):
        print("Você tem {} de {} tentativas " .format(rodada, tentativas))
        chute = int(input("Digite um numero entre 0 e 100: "))
        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if (acertou):
            print("Voce acertou o numero! Total de Pontos {}".format(totalp))
            break
        else:
            if(maior):
                print("VocÊ errou o numero, você digitou oum numero maior")
            if (menor):
                print("Você errou o numero, você digitou um numero menor!")
            perdidos = abs(chute - numero_secreto)
            totalp = abs(totalp - perdidos)

    if (numero_secreto != chute):
        print("O numero sorteado é: {}, total de pontos {}".format(numero_secreto, totalp))

    print("***********")
    print("Fim do Jogo")
    print("***********")