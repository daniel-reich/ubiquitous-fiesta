
def primorial(n):
    primes = []
    counter = 2
    while len(primes) < n:
        if counter == 2:
              primes.append(counter)
        elif all(counter % i for i in range(2, counter)) == True:
            primes.append(counter)
        counter += 1
    result = 1
    for i in primes:
        result *= i
    return result

