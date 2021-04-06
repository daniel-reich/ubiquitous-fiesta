
def prime_gaps(g, a, b):
    x,y=[],[]
    if g==11:
        return None 
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                x.append(num)
    for i in range(len(x)-1):
        if abs(x[i]-x[i+1])==g:
            y.append([x[i],x[i+1]])
    if len(y)==0:
        return None
    return y[0]

