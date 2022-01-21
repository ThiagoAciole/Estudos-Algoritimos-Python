jogador={}
gols=list()
jogador["nome"]=str(input("Nome do Jogador: "))
partida=int(input("Quantas Partidas Jogadas? "))
soma=0
for v in range(0,partida):
    gols.append(int(input(f"    Quantas Gols na  Partida na {v+1}: ")))
    jogador["gols"]=gols[:]
    jogador["total"]=sum(gols)
print("-="*30)
print("MOSTRAGEM 1")
print(jogador)
print("-="*30)
print("MOSTRAGEM 2")
for k, v in jogador.items():
    print(f"O campo {k} é Igual {v}")
print("-="*30)
print("MOSTRAGEM 3")
print(f"O Jogador{jogador['nome']} jogou {partida} partidas")
for i, v in enumerate(jogador["gols"]):
    print(f"    => Na Partida {i+1} {jogador['nome']}, Fez {v} Gols. ")
print(f"Foi um Total de {jogador['total']} gol