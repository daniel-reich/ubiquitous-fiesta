
def fac(n):
    f = []
    for i in range(1,n):
        if n % i == 0:
            f.append(i)
    return f
​
def num_type(n):
    f = fac(n)
    if sum(f) == n:
        return 'Perfect'
    
    if sum(fac(sum(f))) == n:
        return 'Amicable'
    
    return 'Neither'

