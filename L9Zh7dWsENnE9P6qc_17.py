
def josephus(people):    
    if people == 1: return people   
    k=2
    a = list(range(people)) 
    z=0    
    while len(a)>1:
        b = [i for i in a if (a.index(i) + 1 + z) % k == 0]                           
        z = (z + len(a)) % k
        a=[i for i in a if not i in b]               
    return a[0]+1

