
def how_bad(n):
    a=bin(n)
    count=0
    for i in str(a):
        if i=='1':
            count+=1
    x=['Evil' if count%2==0 else "Odious" ]
    y=['t' if count%i==0 else 'f' for i in range(2,count)]
    if count==1:
        return x
    elif 't' not in y:
        x.append( "Pernicious")
        return x
    else:
        return x

