cont=0
for c in range(0,7):
    n=int(input())
    cap=str(input()).upper()
    
    if cap== "G":
        cont+= n*16
    if cap== "P":
     cont+= n*10
print(cont)
print((cont*2)//7)   
