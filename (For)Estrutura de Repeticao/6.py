maior=0
nomemaior=""
count=0
totf=0
for c in range(1,5):
    print("-----{}ª Pessoa------".format(c))
    nome=str(input("NOME? "))
    idade=int(input("IDADE? "))
    sexo=str(input("SEXO [M/F]: "))
    count=(count+idade)/c
    if c==1 and sexo == "M" or "m":
        maior=idade
        nomemaior=nome
    if sexo =="Mm" and idade>maior:
        maior=idade
        nomemaior=nome
    if sexo == "Ff" and idade <20:
        totf+=1    
print("A Média de Idade do Grupo é de {}".format(count))   
print("o Homem Mais Velho tem {} anos e seu nome é{}.".format(maior,nomemaior))
print("Temos {} Mulheres com menos de 20 anos".format(totf))