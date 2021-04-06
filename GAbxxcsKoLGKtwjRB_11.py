
def sum_primes(lst):
    return sum(list(filter(lambda x: (x > 1 and all(x % y != 0 for y in range(2, x))), lst))) if len(lst) > 0 else None

