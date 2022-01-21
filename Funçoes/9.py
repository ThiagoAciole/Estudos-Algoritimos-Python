def leiaint(msg):
    valor=0
    n=str(input(msg))
    if n.isnumeric():
        valor=int(n)
        print(f"O NUMERO INTEIRO É {n}") 
    else:
        print('\033[0;31mERRO ESTE NUMERO NÃO É INTEIRO\033[31m')
    return valor


n=leiaint("Digite um numero:")
   
