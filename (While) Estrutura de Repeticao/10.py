cont=0
soma=0
while True:
    n=int(input("Digite Um Numero(999 para parar)"))
    if n==999:
        break
    cont+=1
    soma+=n
print("A Soma dos {} valores foi {}".format(cont,soma))    