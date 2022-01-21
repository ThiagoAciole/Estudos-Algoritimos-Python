maioridade=0
menoridade=0
for c in range(0,7):
    num=int(input("Em que ano essa pessoa ? "  ))
    num2=(num-2021)*-1
    if num2>=18:
        maioridade+=1
    else:
        menoridade+=1    

print("Ao todo tivemos {} pessoas maiores de idade ".format(maioridade))
print("E tivemos {} pessoas menores de idade ".format(menoridade))