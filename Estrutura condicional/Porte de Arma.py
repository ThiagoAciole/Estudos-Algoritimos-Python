nacionalidade=input()
ocupacao=input()
quant_arm=int(input())
calibre=int(input())

if nacionalidade == "E" and quant_arm == 0:
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "M":
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "T" or ocupacao == "O" and quant_arm == 1 and calibre == 22:
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "C" and quant_arm == 2 and calibre == 22 or calibre == 38 :
    print("Liberado")
else:
    print("Barrado")    
     