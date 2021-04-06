
def is_powerful(number):
    factors, primes, prime_factors = [], [], []
    for i in range(1,number,1):
        if number % i == 0:
            factors.append(i)
    for i in range(2,number,1):
        flag = True
        for i1 in range(2,number,1):
            if i == i1:
                pass
            elif i % i1 == 0:
                flag = False
        if flag == True:
            primes.append(i)
    for i in primes:
        if i in factors:
            prime_factors.append(i)
    flag = True
    for i in prime_factors:
        if i**2 not in factors:
            flag = False
    if flag == True:
        return True
    return False

