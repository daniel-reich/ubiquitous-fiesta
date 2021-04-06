
def dna_to_rna(dna):
    x=[]
    index=0
    d=''
    for i in dna:
        if i=="A":
            index=0
            x.insert(index,"U")
            index=index+1
        elif i=="T":
            index=0
            x.insert(index,"A")
            index=index+1
        elif i=="G":
            index=0
            x.insert(index,"C")
            index=index+1 
        elif i=="C": 
            index=0
            x.insert(index,"G")
            index=index+1 
    for p in x:
        d=p+d
    return d

