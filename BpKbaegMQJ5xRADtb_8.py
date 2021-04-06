
def is_unprimeable(num):
    def isprime(prime):
        if prime <= 1:
            return False
        for i in range(2, prime):
            if prime % i == 0:
                return False
        return True
    if isprime(num):
        return "Prime Input"
    primes = []
    listed = [i for i in str(num)]
    for index in range(len(listed)):
        for digit in range(10):
            listed[index] = str(digit)
            if isprime(int("".join(listed))):
                primes.append(int("".join(listed)))
                
            else:
                listed = [i for i in str(num)]
    if primes == []:
        return "Unprimeable"
    return sorted(primes)

