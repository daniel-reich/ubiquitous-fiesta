
def reverse_complement(n):
    a=[]
    b=list(n)
    for i in n:
        if i=="A":
            a.append("U")
        elif i=="U":
            a.append("A")
        elif i=="G":
            a.append("C")
        elif i=="C":
            a.append("G")
    x="".join(a)
    return x[::-1]

