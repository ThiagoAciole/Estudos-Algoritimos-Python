maior=0
menor=0
cont=0
soma=0
m=""
while m in "Ss":
    n=int(input("digite um Numero? "))
    soma+=n
    cont+=1
    m=str(input("Quer Continuar? [S/N] "))
    if cont==1:
        maior=n
        menor=n
    else:
        if cont < maior:
            maior=n
        if cont > menor:
            menor=n 
media=soma/cont
print("Voce Digitou {} numeros é a media foi {}".format(cont,media)) 
print("O maior valor foi {} e o menor foi {}".format(maior, menor))  