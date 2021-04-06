
def next_prime(num):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    if num in primes:
        return num
    for i in primes:
        if i > num:
            return i

