from random import randint
num= randint(0,10)
num1= randint(0,10)
num2= randint(0,10)
lista=[]
lista.append(num)
lista.append(num1)
lista.append(num2)
count=0
for p, v in enumerate(lista):
    count+=v
    print(f"o numero {v} está na posição {p+1}")
print(f"A Soma dos Numeros da Lista é {count}")