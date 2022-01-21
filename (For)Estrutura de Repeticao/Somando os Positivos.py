soma = 0
n=int(input())
n1=int(input())

if n>n1:
    x=n
    n=n1
    n1=x
for c in range(n, n1+1):
    if c>0:
        soma = soma + c
print(soma)