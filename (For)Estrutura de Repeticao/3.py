num=int(input("Digite um Numero? "))
for c in range(1,num +1):
    if num % c == 0:
        print("\033[1;32m", end=" ")
    else:
        print("\033[1;31m", end=" ") 
    print(c, end=" ")