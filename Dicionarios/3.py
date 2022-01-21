print("-="*30)
print("                     FICHA DE TRABALHO                 ")
print("-="*30)
dados={}
dados['nome']=input("Nome: ")
Ano_nacimento=int(input(f"Ano de Nascimento : "))
dados['idade']=2021-Ano_nacimento
dados['ctps']=int(input("Carteira de Trabalho: "))
if dados['ctps']!=0:
    dados['contratação']=int(input("Ano De contratação:  "))
    dados['Salario']=int(input("Salario: R$  "))
    dados['aposentadoria']=(dados['contratação']-Ano_nacimento)+35
print("-="*30)
for k, v in dados.items():
    print(f" => {k} é Igual {v}")

