m=""
lista=[]
impar=[]
par=[]
while True:    
    lista.append(int(input("digite um numero:")))
    m=str(input("Quer Continuar? [S/N] "))    
    
    if m in "Nn":
        break
for i in lista:    
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)      
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=") 
print(lista)
print(par)
print(impar)

