
def product(lst):
    x=[]
    a=list(set(lst))
    x.append(max(a))
    a.remove(max(a))
    if len(a)>=1:
        x.append(max(a))
        return x[0]*x[1]
    else:
        return x[0]**2

