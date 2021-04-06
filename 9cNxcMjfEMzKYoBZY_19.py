
def num_type(n):
    sum_fact = lambda v: sum(i for i in range(1, v) if v%i == 0)
    sf = sum_fact(n)
    return 'Perfect' if sf == n else 'Amicable' if sum_fact(sf) == n else 'Neither'

