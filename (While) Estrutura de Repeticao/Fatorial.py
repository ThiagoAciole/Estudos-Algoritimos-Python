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

def inicio(msg):
    print("-"*40)
    print(f"            {msg}          ")
    print("-"*40)
    return msg

def menu(opcao):
    inicio("MENU PRINCIPAL")
    print("1 - Ver Pessoas Cadastradas ")
    print("2 - Cadastrar nova Pessoa ")
    print("3 - sair ")
    return opcao