from random import randint
lista=[]
jogos=[]
cont=0
c=0
print("-="*30)
print("         SORTEADOR DE NUMEROS PARA MEGA DA VIRADA        ")
print("-="*30)
nf=int(input("Quantos Numeros você quer Sortear? "))
while c<=nf:
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    c+=1
print(f"-=-=-=-=-= SORTEANDO{c}JOGOS =-=-=-=-=-")
for posicao, aposta in enumerate (jogos):
    print(f"JOGO {posicao+1}: {aposta}")