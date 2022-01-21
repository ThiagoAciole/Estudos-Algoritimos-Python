#Conta de Energia
u=float(input())
u1=(u*1.35)
if u1<=35:
    print("35.00")
    print("1.35")
if 0<=u<=99:
    print("{:.2f}".format(u1))
    print(1.35)    
if 100<=u<=299:
    u2=(u*1.55)
    print("{:.2f}".format(u2))
    print(1.55)
if 300<=u<=574:
    u3=(u*1.75)
    u4=(u3*0.10)
    ur=u3+u4
    print("{:.2f}".format(ur))
    print(1.75)
if u>=574:
    u5=(u*2.15)
    u6=u5*0.10
    ur1=u5+u6
    print("{:.2f}".format(ur1))
    print(2.15)
if u1<=35:
    print("{:.2f}".format(35.00))
    print(1.35)