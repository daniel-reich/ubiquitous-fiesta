
def eratosthenes(n):
    def isprime(x):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    return [x for x in range(2, n + 1) if isprime(x)]

