
def one_odd_one_even(n):
    return bool(sum(divmod(n, 10)) % 2)

