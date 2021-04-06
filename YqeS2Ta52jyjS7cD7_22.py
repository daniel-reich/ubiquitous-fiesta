
def is_prime(n):
    return all(n % i for i in range(2, n)) and n not in [0, 1]

