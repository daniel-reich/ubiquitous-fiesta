
def prime_gaps(g, a, b):
    primes = [2]
    if b < 2 or a > b:
        return None
    elif b == 2:
        return None
    else:
        for n in range(2, b + 1):
            for m in primes:
                if n % m == 0:
                    break
            else:
                primes.append(n)
        for n in primes.copy():
            if n < a:
                primes.remove(n)
    for n in range(len(primes)):
        try:
            if primes[n+1]-primes[n] == g:
                return [primes[n], primes[n+1]]
        except:
            return None

