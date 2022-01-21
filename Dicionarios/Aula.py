dados={}
dados2=[]
for c in range(0, 3):
    dados['nome']=input("Digite Qual e o seu Nome: ")
    dados['sexo']=str(input("Informe seu Sexo [M/F]? ")).strip() .upper()[0]
    while dados['sexo'] not in "MmFf":
        print("Sexo Invalido!!!")
        dados['sexo']=str(input("Dados Invalidos, Informe seu Sexo : ")).upper()
    dados['idade']=(input("Digite Qual sua idade: "))
    dados2.append(dados.copy())
for e in dados2:
    print(e.values())