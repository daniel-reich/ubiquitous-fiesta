
def complete_factorization(num, start=2):
    for ii in range(start, int(num**0.5) +1):
        if num%ii == 0:
            return [ii] + complete_factorization(num//ii, start=ii)
    return [num] if num != 1 else []

