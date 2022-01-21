num=int(input("Digite um numero: "))
c=num
f=1
while True:
    num=int(input("Digite um numero: "))
    if num==-1:
        break
    c-=1
    f*=c
    
print(f)   