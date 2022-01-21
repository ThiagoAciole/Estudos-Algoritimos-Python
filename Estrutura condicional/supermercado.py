#supermercado
dia=str(input())
preco=float(input())
pg=str(input())
nome=str(input())
if dia== "seg" or "ter" or "qua":
    if pg=="ouro":
        r1=preco/2
        print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r1))
    else:
        r4=preco*2
        print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r4))    

elif dia== "qui" or "sex":
    if 10.00 <= preco <=100.00:
        r2=preco*1/3
        print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r2))
    else:
        r4=preco*2
        print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r4))    
elif dia== "sab":
    if pg=="prata":
        r3=preco*3
        print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r3))
    else:
        r4=preco*2
        print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r4))
else:
    r4=preco*2
    print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, r4))
    
