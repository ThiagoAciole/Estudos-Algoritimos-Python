def voto(ano):
    idade=ano-2021
    if idade > 16:
        return "NEGADO"
    elif 18 >idade <=16 or idade <65:
        return "OPCIONAL"
    else:
        return "OBRIGATORIO"

ano=int(input("Em que Ano Você Nasceu?"))
print(voto(ano))       