sexo=str(input("Informe seu Sexo [M/F]? ")).strip() .upper()[0]
while sexo not in "MmFf":
    sexo=str(input("Dados Invalidos, Informe seu Sexo : ")).upper()
print("Sexo Registrado Com Sucesso vocé Pertence ao Sexo {}".format(sexo))    