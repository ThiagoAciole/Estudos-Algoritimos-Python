
m=""
lista=[]
while True:
    lista.append(int(input("digite um numero:")))
    m=str(input("Quer Continuar? [S/N] "))    
    if m in "Nn":
        break
lista.sort()
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=") 
print(f"você Digitou os valores{lista}")   