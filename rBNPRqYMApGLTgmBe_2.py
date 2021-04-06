
def combinations(k,n):
    total = 1 
    for i in range(int(k)): 
        total = total*(n-i) 
    for i in range(1,k+1): 
        total = total//i 
    return total

