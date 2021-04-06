
def fat_prime(a, b):
    if b < a:
        a, b = b, a
    for x in range(b, a-1, -1):
        if is_prime(x):
            return x
​
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

