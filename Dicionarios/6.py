jogador={}
gols=list()
lista=[]
while True:
    jogador["nome"]=str(input("Nome do Jogador: "))
    partida=int(input("Quantas Partidas Jogadas? "))
    soma=0
    for v in range(0,partida):
        gols.append(int(input(f"    Quantas Gols na  Partida na {v+1}: ")))
        jogador["gols"]=gols[:]
        jogador["total"]=sum(gols)
    lista.append(jogador.copy())
    pergunta=(str(input("Voce quer continuar? [S/N]")))
    if pergunta in"Nn":
        break    
print("-="*30)
print(f'{"Nª":<4}{"NOME":<10}{"GOLS":>8}{"TOTAL":>12}')
print("-"*35)
for i, a in enumerate(lista):
    print(f"{i:<4}",end="")
    for k in a.values():
        print(f"{str(k):<15}",end="")
    print()    

    