
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True
​
def c_fuge(n, k):
    if n == 1 or k == 1:
        return False
    if n == k or n%2 == 0:
        return True
    if is_prime(n):
        return False
    return k%2 == 0

