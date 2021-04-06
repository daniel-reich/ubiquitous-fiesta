
def semiprimes(n):
    '''
    Returns 2 lists of semi-prime numbers < n as per the instructions.
    '''
    is_prime = lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
    primes = [i for i in range(2, n//2+1) if is_prime(i)]
    
    lst1 = []
    lst2 = []
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            semi_p = primes[i] * primes[j]
            if semi_p < n:
                lst1.append(semi_p)
                if i != j:  # not perfect square
                    lst2.append(semi_p)
            elif i == j:
                return (sorted(lst1), sorted(lst2))  # no more possible < n
            else:
                break  # no more in this pass
​
    return (sorted(lst1), sorted(lst2))

