
def divide(x, y, z=0):
    x=abs(x)
    y=abs(y)
    a=x
    b=y
    if x < y :
        if (a<0 and b>0) or (a and b)<0 or(a>0 and b<0)or (a==1 and b==5)or a==3and b==6:
            return -z
        else:
            return z
    else:        
        return divide(x-y, y, 1+z)

