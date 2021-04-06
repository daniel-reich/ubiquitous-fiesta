
def goldbach_conjecture(n):
    if n <= 2:       return []
    if n % 2 == 1:   return []
    for i in range(2, n):
        if is_prime(i):
            if is_prime(n-i):
                return [i,  n-i]
​
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

