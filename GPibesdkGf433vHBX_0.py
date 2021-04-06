
def is_prime(a):return all(a % i for i in range(2, a))
def goldbach_conjecture(n):
    for i in range(2,n):
        if is_prime(i) and is_prime(n-i):return [i,n-i]
    return []

