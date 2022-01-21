dados={}
lista=[]
soma=media=0
while True:
    dados['nome']=input("Nome: ")
    dados['sexo']=str(input("Informe seu Sexo [M/F]? ")).strip() .upper()[0]
    while dados['sexo'] not in "MmFf":
        print("Sexo Invalido!!!")
        dados['sexo']=str(input("Informe seu Sexo [M/F]? ")).upper()
    dados['idade']=int(input("Idade: "))
    soma+=dados['idade']
    lista.append(dados.copy())
    pergunta=(str(input("Voce quer continuar? [S/N]")))
    if pergunta in"Nn":
        break
media=soma/len(lista)
print("-="*30)   
print(f"Ao Todo Temos{len(lista)} Pessoas Cadastradas") 
print(f"A media de idade e de {media:.2f} anos")
for p in lista:
    if p['sexo'] in "Ff":
        print(f"As Mulheres Cadastradas Foram {p['nome']}",end="")
print()   
for p in lista:
    if p['idade']  >= media:
        for k, v in p.items():
            print(f" {k} = {v}",end="")
        print()
print("<<<<ENCERRADO>>>>")            