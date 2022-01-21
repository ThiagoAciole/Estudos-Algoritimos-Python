#Classificando Fotografias
psnr=int(input())
en=str(input())
ex=str(input())

if 80<psnr<=90:
    if en== "boa" or "excelente" and ex=="bem exposta":
        print("para imprimir")
    elif en== "boa" or "excelente" and ex=="subexposta" or "superexposta":
        print("boa")
    else:
        print("marromeno")
    
elif 50<=psnr<=80:
    if en=="excelente" and ex=="bem exposta" or "subexposta" :
        print("boa")
    else:
        print("marromeno")
elif psnr<50:
    if en== "boa" or "excelente" and ex=="bem exposta":
        print("marromeno")
    else:
        print("lixo")
     
          