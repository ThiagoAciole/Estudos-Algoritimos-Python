#Conversão_de_Graus
escala=str(input())
temp=float(input())

if escala=="C" or escala== "c":
     if temp <= -273.00:
        print("Valor de temperatura abaixo do minimo")
     else:
        kc= temp + 273.15
        fc=temp * 1.8 + 32
        print("{:.2f}".format(fc),"F")
        print("{:.2f}".format(kc),"K")
    
if escala=="F" or escala == "f":
        if temp <= -459.67:
            print("Valor de temperatura abaixo do minimo")
        else:
            cf=((temp-32)/1.8)
            kf=((temp-32)*5/9)+273.15
            print("{:.2f}".format(cf),"C")
            print("{:.2f}".format(kf),"K")
       
if escala=="K" or escala == "k":
    if temp <= 0.00:
        print("Valor de temperatura abaixo do minimo")
    else:
        ck= temp-273.15
        fk= (temp-273.15)*1.8+32
        print("{:.2f}".format(ck),"C")
        print("{:.2f}".format(fk),"F")    
    