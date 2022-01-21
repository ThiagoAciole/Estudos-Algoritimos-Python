idade=float(input())
jogo=str(input())

games = ["azar", "mmorpg", "moba", "casual"]

if 0>idade<130:
    print("Idade invalida.")
elif jogo not in games:
    print("Jogo invalido.")     
elif idade>=21 and jogo=="azar":
    print("Pode entrar!")
elif 21>idade<0 and jogo=="azar":
    print("Volte daqui h� alguns anos.")
elif 14<=idade and jogo=="mmorpg":
    print("Pode entrar!")
elif 14>idade<0 and jogo=="mmorpg":
    print("Volte daqui h� alguns anos.") 
elif 10<=idade and jogo=="moba":
    print("Pode entrar!")
elif 10>idade<0 and jogo=="moba":
    print("Volte daqui h� alguns anos.") 
elif 0<=idade<=130 and jogo=="casual":
    print("Pode entrar!")



                     