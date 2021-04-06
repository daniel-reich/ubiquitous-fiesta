
def mark_maths(lst):
    fl=[]
    for el in lst:
        for i in range(len(el)):
            if (el[i]=='+') | (el[i]=='-'):
                oi=i
            if el[i]=='=':
                 ei=i
                 a=int(el[:oi])
                 b=int(el[oi+1:ei])
                 r=int(el[ei+1:])
                 if el[oi]=='+':
                        c=a+b
                        if c==r:
                            fl.append(1)
                        else:
                            fl.append(0)
                 if el[oi]=='-':
                    c=a-b
                    if c==r:
                        fl.append(1)
                    else:
                        fl.append(0)
    fls=str(round((sum(fl)*100)/len(fl),0))
    return fls.split('.')[0]+'%'

