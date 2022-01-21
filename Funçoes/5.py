from random import randint
from time import sleep
def sortea(lista):
   print(f"Os Numeros Sorteados Foram Lista: ",end="") 
   for c in range(0,5):
       n=randint(1,10)
       lista.append(n)
       print(f" {n} ",end="",flush=True)
       sleep(0.2)
   print("Pronto!!!")   

def somapar(lista):
    soma=0
    print(f"OS numeros Pares são",end="")
    for valor in lista:
        if valor%2==0:
            soma+=valor
            print(f" {valor} ",end="")
    print(f"e a Soma deles dá : {soma}",end="")    


num=[]
sortea(num)
somapar(num)