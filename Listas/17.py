m=""
cont=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez",
"onze","doze","treze","catorze","quize","dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
    while True:
        num=int(input("digite um numero entre 0 e 20: "))
        if 0<=num <=20:
            break
        else:
            print("Tente Novamente ==> ", end="")
        if m=="Nn":
            break    

    print(f'==> Você Digitou o Numero {cont[num]} <==')
    m=str(input("Quer continuar? "))
           