maior=0
menor=0
lista=[]
for c in range(0,5):
    lista.append(int(input("digite um numero:")))
   
    if c==0:
        maior=lista[c]
        menor=lista[c]
    else:
        if lista[c] > maior:
            maior=lista[c]
        if lista[c] < menor:
            menor=lista[c] 
print(f"Voce digitou os valores {lista}")
print(f"O maior valor foi {maior} e o menor foi {menor}")