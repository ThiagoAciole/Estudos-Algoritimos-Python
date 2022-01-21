#Bibliotecas
from time import sleep
#Funçoes
def mensagem(msg):
    print("-="*25)
    print(msg)


def contador(a,b,c):
    if c<0:
        c*=-1
    if c==0:
        c=1    
   
    for c in range(a,b+1,c):
        print(f" {c} ", end="", flush=True)
        sleep(0.2)
    
    print("FIM!")  
#Programa Principal
#Contagem 1
mensagem("Contagem De 1 até 10 de 1 em 1")
contador(1,10,1)

#Contagem 2
mensagem("Contagem De 10 até 0 de 2 em 2")
contador(10,0,-2)

#Contagem 3
mensagem("Agora é Sua vez de Personalizar a Contagem!")
inic=int(input("Inicio: "))
fim=int(input("Fim: "))
passo=int(input("passo: "))
print("-="*25)
mensagem(f"Contagem de {inic} até {fim} de {abs(passo)} em {abs(passo)}")

contador(inic,fim,passo)
print("-="*25)