soma=0
num=0
num2=0
count=0
for c in range(7):
    num2=num
    num=float(input())
    soma=soma+num 
    if(num-num2>=0.5) and c!=0:
        count+=1
    
print("R$ {:.2f}".format(soma))

print(count)   
        

