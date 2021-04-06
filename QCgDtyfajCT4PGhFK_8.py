
def prime_factorization(number):
    l, p=[], primes(number)
    while number not in p+[1]:
        for i in p:
            if number%i==0:
                l.append(i)
                number = int(number/i)
    if number==1:
        return sorted(l)
    return sorted(l + [number])
​
def primes(x):
    l = []
    for i in range(2, x + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            l.append(i)
    return l

