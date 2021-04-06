
def c_fuge(n, k):
    if n == 1 or k == 1 or n-k == 1 or n < k:
        return False
    elif n == k:
        return True
    elif n % k == 0:
        return True
    missing = n - k
    check = 0
    primes = get_primes(n)
    if k == get_sum(primes) or missing == get_sum(primes):
        return True
    for i in range(len(primes)):
        if k % primes[i] == 0 and missing % primes[i] == 0:
            check += 1
    if check == 0:
        return False
    else:
        return True
​
​
def get_primes(n):
    primes = []
    count = 0
    for i in range(2, n-2):
        if n % i == 0:
            for j in range(2, i-1):
                if i % j == 0:
                    count += 1
            if count == 0:
                primes.append(i)
    return primes
​
​
def get_sum(primes):
    total = 0
    for i in range(len(primes)):
        total += primes[i]
    return total

