
def smith_type(n):
    if isprime(n):
        return "Trivial Smith"
    elif issmith(n):
        return "Oldest Smith" if issmith(n-1) else "Youngest Smith" if issmith(n+1) else 'Single Smith'
    else:
        return "Not a Smith"
​
def issmith(n):
    p = sum(prime_factors(n))
    while len(str(n)) >= 2:
        n = sum([int(i) for i in str(n)])
    while len(str(p)) >= 2:
        p = sum([int(i) for i in str(p)])
    return n == p
​
def prime_factors(n):
    lst = []
    for i in range(2, int(n / 2) + 1):
        while n % i == 0:
            lst.append(i)
            n //= i
    return (lst)
​
def isprime(n):
    return n >= 2 and all(n % i for i in range(2,n//2+1))

