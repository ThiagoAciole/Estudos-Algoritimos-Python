count=0
m=""
lista=[]
while m in "Ss":
    lista.append(int(input("digite um numero:")))
    count+=1
    m=str(input("Quer Continuar? [S/N] "))
lista.sort(reverse=True)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=") 
print(f"Você Digitou {count} valores")
print(f"A lista com valores em decrescente {lista}")   
if 5 in lista:
    print("o numero 5 está sim na lista")
else:
    print("o numero 5 não está na lista")    