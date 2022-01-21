expr= str(input("Digite a Espressão: "))
lista=[]
for c in expr:
    if c=="(":
        lista.append("(")
    elif c == ")":
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista)==0:
    print("Sua Expressão é Valida")
else:
   print("Sua Expressão é invalida")             