
def get_prime_factors(n):
    f = 2
    factors = []
    limit = n // 2
    while f <= limit:
        if n % f == 0:
            factors.append(f)
            n /= f
        else:
            f += 1
    if f > limit and not factors: factors.append(n)
    return factors
​
​
def get_sum_type(a, b):
    a_f = get_prime_factors(a)
    b_f = get_prime_factors(b)
​
    if sum(a_f) == sum(b_f):
        if len(a_f) == len(set(a_f)) and len(b_f) == len(set(b_f)):
            return 3
        else:
            return 2
    elif sum(set(a_f)) == sum(set(b_f)):
        return 1
    else:
        return False
​
​
def ruth_aaron(n):
    for n_pair in [n - 1, n + 1]:
        sum_type = get_sum_type(n, n_pair)
        if sum_type:
            pair_type = 'Ruth' if n < n_pair else 'Aaron'
            return [pair_type, sum_type]
    return False

