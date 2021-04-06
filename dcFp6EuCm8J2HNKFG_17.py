
def func(lst):    
    a,c,d = [], [], []
    c.append(len(lst))    
    a= lst
    t=0
    while t<len(lst):    
        for i in a:
            if type(i)==list:
                c.append(len(i))
                d=d+i
        a=d
        t+=1
    return sum(c)

