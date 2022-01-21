from random import randint
computador=randint(0,10)
print("========== SERA QUE VOCÊ ADIVINHA QUAL NUMERO EU ESTOU PENSANDO?============")
palpite=0
tentativas=0
while palpite != computador:
    palpite=int(input("Escolha um numero? "))
    if palpite == computador:
        print("Você Acertou!!!")
    else:
        if palpite > computador:
            print("Você Digitou um numero Maior ")
        elif palpite < computador:
            print("Você Digitou um numero Menor")
    tentativas+=1
print("Você teve {} tentativas".format(tentativas))    