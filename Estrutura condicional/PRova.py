dia=int(input())
estd=int(input())
soc=int(input())

if 1<=dia<=4 and estd==0 and soc==0:
    print("COMUM: R$ 15.00")
    

elif 5<=dia<=7 and estd==0 and soc ==0:
      print("COMUM: R$ 30.00")

elif 1<=dia<=4 and estd==1 and soc==0:
      estd1=15.00 - (15*0.30)
      print("ESTUDANTE: R$ {:.2f}".format(estd1))                 

elif 5<=dia<=7 and estd==0 and soc==1:
      soc1=30.00 - (30*0.20)
      print("SOCIO: R$ {:.2f}".format(soc1))
   

