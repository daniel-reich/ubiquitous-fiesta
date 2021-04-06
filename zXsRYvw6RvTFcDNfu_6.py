
def prime_factors(n):
    '''
    Returns a list of the prime factors of integer n as per above
    '''
    primes = []
    for i in range(2, int(n**0.5) + 1):
​
        while n % i == 0:
            primes.append(i)
            n //= i
​
    return primes + [n] if n > 1 else primes
​
def ruth_aaron(n):
    '''
    Returns an appropriate message if n is a type 1, 2 or 3 Ruth or Aaron pair
    as described above, or False if it is neither.
    '''
    ns = [n-1, n, n+1]
    type_2 = [sum(prime_factors(a)) == sum(prime_factors(b)) for a, b in zip(*(ns, ns[1:]))]
    type_1 = [sum(set(prime_factors(a))) == sum(set(prime_factors(b))) for a, b in zip(*(ns, ns[1:]))]
    type_3 = [type_1[i] and type_2[i] for i in range(len(type_1))]
​
    results = (type_3, type_2, type_1)
    for i, result in enumerate(results):
        if result[0]:
            return ['Aaron', 3 - i]
        elif result[1]:
            return ['Ruth', 3 - i]
​
    return False

