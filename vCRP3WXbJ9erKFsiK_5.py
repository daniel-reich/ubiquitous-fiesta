
def dif_ciph1(inpt):
    x,res,y,=[],'',[]
    for i in inpt:            
        if i==' ':
            x.append(ord(i))
        else:
            x.append(ord(i))
    a=x[0]
    x=x[::-1]
    for i in range(len(x)-1):
        y.append(x[i]-x[i+1])
    y=y+[a]  
    return y[::-1]   
def dif_ciph2(inpt):
    z,res=[],''
    a=inpt[0]+inpt[1]
    z.append(inpt[0])
    z.append(a)
    for i in range(2,len(inpt)):
        if type(inpt[i])==int:
            b=inpt[i]+a
            z.append(b)
            a=b        
    for i in z:
        res+=chr(i)
    return res    
def dif_ciph(inpt):
    for i in inpt:
        if type(i)==str:
            return dif_ciph1(inpt)
        else:
            return dif_ciph2(inpt)

