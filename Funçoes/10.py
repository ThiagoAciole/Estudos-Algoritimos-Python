def notas(*n, situação=False):
    r={}
    r["total"]= len(n)
    r["maior"]= max(n)
    r["menor"]= min(n)
    r["media"]= sum(n)/len(n)
    if situação:
        if r['media']<7.0:
            r['situação']="Reprovado"
        else:
            r['situação']="aprovado"
    return r



#Programa Principal
resp=notas(5.5,7.2,9.8,situação=True)
print(resp)