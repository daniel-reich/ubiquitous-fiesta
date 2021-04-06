
def simplify_sqrt(n):
    a = 1
    b = 1
​
    if natural_sqrt(n):
        return (natural_sqrt(n), 1)
​
    for i in range(1, int(n/2+1)):
        if n%i==0 and natural_sqrt(i):
            a = natural_sqrt(i)
            b = n/i
​
    return (a, int(b))
​
def natural_sqrt(n):
    if n == 1:
        return 1
        
    for i in range(1, n//2+1):
        if i*i == n:
            return i
    
    else: return False

