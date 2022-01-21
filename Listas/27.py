matriz=[[0,0,0], [0,0,0], [0,0,0]]
somap=0
mai=0
somac=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input("Digite um valor:"))
print("-="*30)
for l in range(0,3):
    for c in range(0,3):
        print([matriz[l][c]], end="")
        if matriz[l][c]%2==0:
            somap+=matriz[l][c]
    print()            
print(f"A Soma dos Pares e {somap}")
for l in range(0,3):
    somac+=matriz[l][2]
print(f"A Soma dos valores da terceira coluna e {somac}")
for c in range(0,3):
    if c==0:
        mai=matriz[1][c]
    else:
        if  matriz[1][c]> mai:
            mai=matriz[1][c]
print(f"o maior valor da segunda linha é {mai}")            