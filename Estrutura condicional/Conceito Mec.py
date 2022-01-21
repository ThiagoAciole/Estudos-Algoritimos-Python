#Conceito Mec
l=int(input())
p=int(input())

r= p / l

if r <= 8:
    print("A")
elif 9 <= r <= 12:
    print("B")
elif 13 <= r <= 18:
    print("C")
elif r > 18:
    print("D")