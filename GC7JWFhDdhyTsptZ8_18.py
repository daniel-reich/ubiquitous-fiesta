
def sexy_primes(n, limit):
​
    aux = []
    primes = []
​
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                aux.append(i)
​
    for k in range(2, limit):
        if k not in aux:
            primes.append(k)
​
    sexy_pair = []
    sexy_triplets = []
​
    if n == 2:
        for i in range(0, len(primes)):
            for j in range(0, len(primes)):
                if primes[i] + 6 == primes[j]:
                    sexy_pair.append((primes[i], primes[j]))
        return sexy_pair
​
    if n == 3:
        for i in range(0, len(primes)):
            for j in range(0, len(primes)):
                for k in range(0, len(primes)):
                    if primes[i] + 6 == primes[j] and primes[i] + 12 == primes[k]:
                        sexy_triplets.append((primes[i], primes[j], primes[k]))
        return sexy_triplets

