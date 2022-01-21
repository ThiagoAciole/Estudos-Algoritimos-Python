ficha=[]
print("-="*30)
print("      CADERNETA DE NOTAS DOS ALUNOS       ")
print("-="*30)
while True:
    nome=(str(input("NOME: ")))
    nota1=(float(input("NOTA 1:")))
    nota2=(float(input("NOTA 2:"))) 
    media=(nota1+nota2)/2
    ficha.append([nome, [nota1,nota2],[media]])
    pergunta=(str(input("Voce quer Adicionar Algum Elemento? [S/N]")))
    if pergunta in"Nn":
        break
print("-="*30)
print(f'{"Nª":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-"*28)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
