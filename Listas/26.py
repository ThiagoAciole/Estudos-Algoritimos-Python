valores=[[],[]]
valor=0
for v in range(1,8):
    valor=int(input(f"Digite o {v}ª numero: "))
    if valor%2==0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)  
valores[0].sort()
valores[1].sort()
print(f"Os numeros pares são {valores[0]}")    
print(f"Os numeros impares são {valores[1]}") 
