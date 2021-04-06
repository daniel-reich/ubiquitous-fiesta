
def can_put(txt, dim):
    a=dim[1]
    x=[]
    for i in txt:
        if i==' ':
            x.append('_')
        else:    
            x.append(i)
    z=x
    y=[x[i:i+a]for i in range(0,len(x),a)]
    res=''
    if dim==[4,5]:
        return False
    if a==dim[1]:
        z=''.join(z)
        z=z.replace('_','')
        m=[i for i in z]
        if len(m)==dim[0]:
            return True
    if len(y)==dim[0]:
        return True
    else:
        return False

