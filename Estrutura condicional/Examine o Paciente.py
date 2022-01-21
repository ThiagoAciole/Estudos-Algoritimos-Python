#Examine o Paciente
temp=float(input())
std=str(input())


if temp>=37 and std=="S":
    print("Exames Especiais")
elif temp>=37 and std=="N":
    print("Exames Basicos")
elif temp<37 and std=="S":
    print("Exames Basicos")
elif temp<37 and std=="N":
    print("Liberado") 
elif temp>=37 and std != "S" or "N":
    print("Erro")                 