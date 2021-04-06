
def coconut_translator(txt):
    x,y,res=[],[],''
    d={0:'c',1:'o',2:'c',3:'o',4:'n',5:'u',6:'t',7:'s'}
    txt1=bytearray(txt, "utf8")
    for i in txt1:
        i=bin(i)
        if len(i)==9:
            a=i.replace('b','')
        else:
            a=i.replace('b','0')
        x.append(a)
    for i in x:
        for j,v in enumerate(i):
            if j in d:
                if v=='0':
                    res+=d[j]
                else:
                    res+=d[j].upper()
        y.append(res)
        res=''
    return ' '.join(y)

