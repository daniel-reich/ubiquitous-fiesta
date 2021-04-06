
def prime_divisors(n):
    res = set()
    for i in range(2, int(n**0.5) + 1): 
        while not n%i: 
            res.add(i) 
            n //= i
    if n > 1:
        res.add(n)
    return sorted(res)

