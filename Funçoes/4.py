from time import sleep

def maior(* num):
    print(f"Analizando Os Valores Passados ....")
    cont=mai=0
    for valor in num:
        print(f" {valor} ", end="" ,flush=True)
        sleep(0.2)
        if cont ==0:
            mai=valor
        else:
            if valor > mai:
                mai=valor 
        cont+=1
    print()
    print(f"O Maior Valor é {mai}")


maior(1,2,3,4,5,6,7)