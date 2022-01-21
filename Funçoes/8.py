def ficha(nome="<desconhecido>", gols=0):
    print("-"*30)
    print(f"O Jogador {nome} fez {gols} gol(s) no Campeonato")

nome=str(input("Nome do Jogador: "))
gol=str(input("Numero de Gols: "))
if gol.isnumeric():
    gol=int(gol)
else:
    gol=0    
if nome.strip()=="":
    ficha(gols=gol)
else:    
    ficha(nome,gol)