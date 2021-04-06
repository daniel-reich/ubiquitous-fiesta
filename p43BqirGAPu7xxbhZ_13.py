
def diamond(carat):
    a,r=[],[]    
    if carat %2==0:
        for i in range(carat-1):
            a.append([])
        for i in range(carat-1):
            for j in range(carat):
                a[i].append(0)
        for i in range(carat-1):
            a[i][abs((carat-2)//2-i)]=1
            a[i][-1-abs((carat-2)//2-i)]=1 
        r.append(a)
        r.append("good cut")  
    else:  
        for i in range(carat):
            a.append([])
        for i in range(carat):
            for j in range(carat):
                a[i].append(0)
        for i in range(carat):
            a[i][abs((carat-1)//2-i)]=1
            a[i][-1-abs((carat-1)//2-i)]=1
        r.append(a)
        r.append("perfect cut")     
    return r

