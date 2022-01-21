n=int(input("Digite Um Numero(999 para parar)"))
n=0
cont=0
soma=0
while n!=999:
    cont+=1
    soma+=n
    n=int(input("Digite Um Numero(999 para parar)"))
print("A Soma dos {} valores foi {}".format(cont,soma))    