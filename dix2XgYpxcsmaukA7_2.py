
def express_factors(n): 
    factors = [] 
    for i in range(2, int(n**0.5) + 1):
        group = []
        while n % i == 0:
            group.append(i) 
            n //= i
        if group:
            d = group[0]
            if len(group) > 1:
                factors.append('{}^{}'.format(d, len(group)))
            else:
                factors.append(str(d))
    if n != 1:
        factors.append(str(n))
    return ' x '.join(factors)

