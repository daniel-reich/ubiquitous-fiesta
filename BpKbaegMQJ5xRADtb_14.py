
def is_prime(n):
    return n > 1 and (n == 2 or (n%2 != 0 and all(n%i for i in range(3, int(n**0.5 + 1), 2))))
​
def is_unprimeable(num):
    if is_prime(num): return 'Prime Input'
    ns, primes = str(num), set()
    for i in range(len(ns)):
        for ch in '0123456789':
            n = int(ns[:i] + ch + ns[i+1:])
            if is_prime(n):
                primes.add(n)
    return 'Unprimeable' if len(primes) == 0 else sorted(list(primes))

