while True:
    n = int(input())
    if 1 <= n <= 9:
        break
    else:
        print("Insira um número inicial entre 1 e 9")

while True:
    m = int(input())
    if 1 <= m <= 9:
        break
    else:
        print("Insira um número final entre 1 e 9")

if n > m:
    print("Nenhuma tabuada nesse intervalo")
    exit(0)

for y in range(n, m + 1):
    for x in range(1, 10):
        s = y * x
        if x == 9:
            print(f"{y} x {x} = {s}")
            print()
        else:
            print(f"{y} x {x} = {s}")