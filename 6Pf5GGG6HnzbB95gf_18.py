
def find_factors(n):
    if n < 1:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]

