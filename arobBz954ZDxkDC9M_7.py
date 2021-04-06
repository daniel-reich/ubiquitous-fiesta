
def isPrime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False
​
def next_prime(num):
    if isPrime(num):
        return num
    else:
        while not isPrime(num):
            num += 1
    return num

