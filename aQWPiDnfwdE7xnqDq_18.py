
def drange (*x):
    if len(list(x)) == 1:
        return tuple(range(x[0]))
    elif len(list(x)) == 2:
        return tuple(range(x[0],x[1]))
        
    else:
​
        z=[]
        top=x[0]
        while top < x[1]:
            z.append(round(top,3))
            top += x[2]
        return tuple(z)

