
def little_big(n):
    
    l1 = [i for i in range(5,101)]
    l2 = []
    l3 = []
    a = 50
    b = 0
    
    while b < 20:
        a = a * 2
        l2.append(a)
        b = b + 1
    
    for i,j in zip(l1,l2):
        l3.append(i)
        l3.append(j)
    
    for i in l3:
        if l3.index(i) == n-1:
            return i

