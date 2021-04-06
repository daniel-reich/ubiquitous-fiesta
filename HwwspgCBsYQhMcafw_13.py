
def super_digit(n, k):
​
    a, b =list(n), []
    for i in a:
        b.append(int(i))
    tot = (sum(b))*k
    n=str(tot)    
    while len(list(n)) >0:        
        a, b =list(n), []
        for i in a:
            b.append(int(i))
        tot = (sum(b)) 
        n=str(tot)        
        if len(n) == 1:
            break
    return int(n[0])

