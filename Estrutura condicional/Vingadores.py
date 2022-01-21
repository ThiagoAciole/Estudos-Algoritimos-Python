#Vingadores
lista = ["Homem de Ferro", "Hulk", "Capitão América", "Thor", "Gavião Arqueiro", "Viúva Negra"]
vingador = str(input())

if vingador in lista:
 poder = str(input())
 energia = int(input())
if vingador not in lista:
    print("Vingador Inv�lido") 
else:
    if vingador == "Homem de Ferro":
        if poder != "Armadura de Ferro":
            print("Homem de Ferro NAO conseguiu derrotar Thanos")
        if (poder == "Armadura de Ferro" and energia >= 10):
            print("Homem de Ferro conseguiu derrotar Thanos")
        if poder == "Armadura de Ferro" and energia < 10:
            print("Homem de Ferro NAO conseguiu derrotar o Thanos, chamem outro Vingador")
        if poder == "For�a Bruta":
            print("Esse � o poder do Hulk")
        if poder == "Escudo":
            print("Esse � o poder do Capit�o Am�rica")
        if poder == "Martelo":
            print("Esse � o poder do Thor")
        if poder == "Arco e Flecha":
            print("Esse � o poder do Gavi�o Arqueiro")
        if poder == "Inteligencia":
            print("Esse � o poder do Vi�va Negra")

    if vingador == "Hulk":
        if poder != "For�a Bruta":
            print("Hulk NAO conseguiu derrotar Thanos")
        if poder == "For�a Bruta" and energia >= 5:
            print("Hulk conseguiu derrotar Thanos")
        if poder == "For�a Bruta" and energia < 5:
            print("Hulk NAO conseguiu derrotar o Thanos, chamem outro Vingador")
        if poder == "Armadura de Ferro":
            print("Esse � o poder do Homem de Ferro")
        if poder == "Escudo":
            print("Esse � o poder do Capit�o Am�rica")
        if poder == "Martelo":
            print("Esse � o poder do Thor")
        if poder == "Arco e Flecha":
            print("Esse � o poder do Gavi�o Arqueiro")
        if poder == "Inteligencia":
            print("Esse � o poder do Vi�va Negra")

    if vingador == "Capit�o Am�rica":
        if poder != "Escudo":
            print("Capit�o Am�rica NAO conseguiu derrotar Thanos")
        if poder == "Escudo" and energia >= 7:
            print("Capit�o Am�rica conseguiu derrotar Thanos")
        if poder == "For�a Bruta":
            print("Esse � o poder do Hulk")
        if poder == "Escudo" and energia < 7:
            print("Capit�o Am�rica NAO conseguiu derrotar o Thanos, chamem outro Vingador")
        if poder == "Armadura de Ferro":
            print("Esse � o poder do Homem de Ferro")
        if poder == "Martelo":
            print("Esse � o poder do Thor")
        if poder == "Arco e Flecha":
            print("Esse � o poder do Gavi�o Arqueiro")
        if poder == "Inteligencia":
            print("Esse � o poder do Vi�va Negra")

if vingador == "Thor":
    if poder != "Martelo":
        print("Thor NAO conseguiu derrotar Thanos")
    if vingador == "Thor" and poder == "Martelo" and energia >= 4:
        print("Thor conseguiu derrotar Thanos")
    if poder == "For�a Bruta":
        print("Esse � o poder do Hulk")
    if poder == "Thor" and energia < 4:
        print("Thor NAO conseguiu derrotar o Thanos, chamem outro Vingador")
    if poder == "Escudo":
        print("Esse � o poder do Capit�o Am�rica")
    if poder == "Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
    if poder == "Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
    if poder == "Inteligencia":
        print("Esse � o poder do Vi�va Negra")

elif vingador == "Gavi�o Arqueiro":
    if poder != "Arco e Flecha":
        print("Gavi�o Arqueiro NAO conseguiu derrotar Thanos")
    if vingador == "Gavi�o Arqueiro" and poder == "Arco e Flecha" and energia >= 12:
        print("Gavi�o Arqueiro conseguiu derrotar Thanos")
    if poder == "Gavi�o Arqueiro" and energia < 12:
        print("Gavi�o Arqueiro NAO conseguiu derrotar o Thanos, chamem outro Vingador")
    if poder == "For�a Bruta":
        print("Esse � o poder do Hulk")
    if poder == "Escudo":
        print("Esse � o poder do Capit�o Am�rica")
    if poder == "Martelo":
        print("Esse � o poder do Thor")
    if poder == "Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
    if poder == "Inteligencia":
        print("Esse � o poder do Vi�va Negra")

if vingador == "Vi�va Negra":
    if poder != "Intelig�ncia":
        print("Vi�va Negra NAO conseguiu derrotar Thanos")
    if poder == "Intelig�ncia" and energia >= 20:
        print("Viuva Negra conseguiu derrotar Thanos")
    if poder == "Intelig�ncia" and energia < 20:
        print("Vi�va Negra NAO conseguiu derrotar Thanos, chamem outro Vingador")
    if poder == "For�a Bruta":
        print("Esse � o poder do Hulk")
    if poder == "Escudo":
        print("Esse � o poder do Capit�o Am�rica")
    if poder == "Martelo":
        print("Esse � o poder do Thor")
    if poder == "Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
    if poder == "Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")

    