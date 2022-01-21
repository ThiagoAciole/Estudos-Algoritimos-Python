nome=input("digite um nome: ")
idade=input("qual a idade dele: ")
test=list()
test.append(nome)
test.append(idade)
print(test)
galera=list()
galera.append(test[:])
while True:
    pergunta=(str(input("Voce quer Adicionar Algum Elemento? [S/N]")))
    if pergunta in"Nn":
        break
    else:
        test[0]=input("Qual Nome Você quer adicionar?")
        test[1]=input("Qual a idade dele(a)?")
        galera.append(test[:])
        print(galera)
       