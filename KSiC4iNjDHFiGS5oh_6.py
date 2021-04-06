
def is_super_d(n):
    x=[]
    for i in range(2,10):
        a=str(i*pow(n,i))
        if a.count(i*str(i))>=1:
            x.append(i)
            break
    if len(x)>0:
        return "Super-{} Number".format(str(x[0]))
                                    
    return "Normal Number"

