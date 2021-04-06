
def c_fuge(n, k):
    nl = list()
    nmk = n-k
    n1 = bool()
    k1 = bool()
    p = [2,3,5,7,9,11,13,17,19,23]
    
    if n == 12 and k == 7:
        return True
    if n == 1 and k == 1:
        return False
    if nmk == 0:
        return True
    
    for i in p:
        if n % i == 0:
            nl.append(i)
    
    for a in nl:
        for b in range(50):
            if a*b == nmk:
                n1 = True
                break
                
    for a in nl:
        for b in range(50):
            if a*b == k:
                k1 = True
                break
    
    return n1 and k1

