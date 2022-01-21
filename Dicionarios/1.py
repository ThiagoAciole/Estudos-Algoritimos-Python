dados={}
dados['nome']=input("Nome: ")
dados['media']=float(input(f"Media de {dados['nome']}: "))
if dados['media']<7.0:
    dados['situação']="Reprovado"
else:
    dados['situação']="aprovado"
print(f"O Nome é Igual a {dados['nome']}")
print(f"Média é Igual a {dados['media']}")
print(f"Situação {dados['situação']}")