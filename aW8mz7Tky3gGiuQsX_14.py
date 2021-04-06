
def is_powerful(n):
    start = n
    res = [] 
    while n % 2 == 0: 
        res.append(2) 
        n = n // 2 
    for i in range(3, int(n**0.5) + 1, 2): 
        while n % i == 0: 
            res.append(i) 
            n = n // i 
    return all(start%(i**2) == 0 for i in res + [n])

