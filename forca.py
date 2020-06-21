def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    palavra_chave = "banana"
    enforcou = False
    acertou = False
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")

        index = 0
        for letra in palavra_chave:
            if (chute == letra):
                print(("Encontrei a letra {} na posição {}".format(letra, index)))
                index = index + 1
        print("Jogando ")
    



if (__name__ == "__main__"):
    jogar()