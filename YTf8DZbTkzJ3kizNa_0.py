
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True
​
def moran(n):
    d = sum(int(i) for i in str(n))
    if n%d:
        return 'Neither'
    return 'M' if is_prime(n//d) else 'H'

