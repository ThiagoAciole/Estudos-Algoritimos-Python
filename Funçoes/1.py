def area(a,b):
    s=a*b
    print(f"A Area de terreno {a}x{b} é de {s}m²")


print("     CONTROLE DE TERRENOS        ")
print("-="*25)
a=float(input("LARGURA (m): "))
b=float(input("COMPRIMENTO (m): "))
area(a,b)