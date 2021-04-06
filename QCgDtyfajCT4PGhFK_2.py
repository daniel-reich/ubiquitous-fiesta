
def prime_factorization(n):
    res = []
    for i in range(2, int(n**0.5) + 1): 
        while not n%i: 
            res.append(i) 
            n //= i
    return res + [n] if n > 1 else res

