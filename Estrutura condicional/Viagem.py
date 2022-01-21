#Viagem
pessoas=int(input())
local=str(input()).upper()
quarto=int(input())
valor1 = 600 + pessoas * 75
valor2 = 900 + pessoas * 75
valor3 = 950 + pessoas * 60
valor4 = 1120 + pessoas * 60
final1 = valor1 / pessoas
final2 = valor2 / pessoas
final3 = valor3 / pessoas
final4 = valor4 / pessoas

if local== "PIPA" and quarto == 2:
    print("{:.2f}".format(valor1))
    print("{:.2f}".format(final1))
elif local== "PIPA" and quarto == 3:
    print("{:.2f}".format(valor2))
    print("{:.2f}".format(final2))
elif local== "FORTALEZA" and quarto == 3:
    print("{:.2f}".format(valor3))
    print("{:.2f}".format(final3))
elif local== "FORTALEZA" and quarto == 4:
    print("{:.2f}".format(valor4))
    print("{:.2f}".format(final4))

