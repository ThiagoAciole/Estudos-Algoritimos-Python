print("=========================================================")
print(">>>>>>>>>>>>>>>>> CALCULADORA DO ACIOLE <<<<<<<<<<<<<<<<<")
print("=========================================================")
valor1=int(input("Digite um Valor ? "))
valor2=int(input("Digite um Valor ? "))
opcoes=0
while opcoes != 5:
    print("     [1] Somar")
    print("     [2] Multiplicar")
    print("     [3] Maior")
    print("     [4] Novos Numeros")
    print("     [5] Sair")
    opcoes=int(input(">>>>>>> Qual Sua Opção? "))
    if opcoes == 1:
        soma= valor1+valor2
        print(" A soma de {} + {} é {}".format(valor1,valor2,soma))
    elif opcoes == 2:
        multiplicar= valor1*valor2
        print(" A multiplicação de {} X {} é {}".format(valor1,valor2,multiplicar))
    elif opcoes == 3:
        if valor1 > valor2:
            maior_valor = valor1
        else:
            maior_valor = valor2 
        print("o Maior Valor é {} ".format(maior_valor)) 
    elif opcoes == 4:
        valor1=int(input("Digite outro Valor ? "))
        valor2=int(input("Digite outro Valor ? "))
print("Está Certo Amigo!!!")