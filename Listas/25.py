dado=[]
dados_gerais=[]
menor=0
maior=0

while True:
    dado.append(str(input("digite um nome: ")))
    dado.append(float(input("qual a peso dele(a)?")))
    if len(dados_gerais)==0:
            maior=dado[1]
            menor=dado[1]
    else:
        if dado[1] > maior:
            maior=dado[1]
        if dado[1] < menor:
            menor=dado[1]
    dados_gerais.append(dado[:])
    dado.clear()
    pergunta=(str(input("Voce quer Adicionar Algum Elemento? [S/N]")))
    if pergunta in"Nn":
        break

for p in dados_gerais:
    if p[1]== maior:
        nome_mai=p[0]
for p in dados_gerais:
    if p[1]== menor:
        nome_men=p[0]        
print(f"Foram cadastradas {len(dados_gerais)} pessoas")
print(f"A pessoa mais pesada doi {nome_mai} com {maior} e a com menor peso foi {nome_men} {menor}")