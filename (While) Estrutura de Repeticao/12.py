print("=================================")
print("10 TERMOS DE UMA PA")
print("=================================")
primeiro=int(input("Qual Primeiro Termo? "))
razão=int(input("Qual a Razão? "))
termo= primeiro
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont<=total:
        print(termo,end=" -> ")
        termo+=razão
        cont+=1
    print("Pausa")
    mais=int(input("Quantos Termos você quer a mais?"))
print("Acabou")    