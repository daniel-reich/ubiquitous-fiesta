
def is_early_bird(_range, n):
    a = []
    for i in range(_range+1):
        a.append(str(i))
    a = ''.join(a)    
        
    n = str(n)
    l = len(n)
    myans = []
    for i in range(len(a)+1):
        t = []
        if a[i:i+l] == n:
            for j in range(i,i+l):
                t.append(j)           
            myans.append(t)        
    
    if len(myans) > 1:
        myans.append('Early Bird!')
    
    return myans

