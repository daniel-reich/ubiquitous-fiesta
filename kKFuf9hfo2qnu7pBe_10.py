
def is_prime(primes, num, left=0, right=None):
    if num == primes[0] or num == primes[len(primes)-1]:
        return "yes"
    right = len(primes) - 1
    left = 0
    while True:
        mid = (right + left) // 2
        if mid == left:
            return "no"
        elif num == primes[mid]:
            return "yes"
        elif num >= primes[0] and num < primes[mid]:
            right = mid
            continue
        elif num > primes[mid] and num <= primes[len(primes)-1]:
            left = mid
            continue
        else:
            pass

