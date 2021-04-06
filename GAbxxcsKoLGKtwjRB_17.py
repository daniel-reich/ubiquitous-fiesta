
def sum_primes(lst):
    if len(lst) != 0:
        res = 0
        for x in lst:
            f_count = 0
            for i in range(1, x):
                if x % i == 0:
                    f_count += 1
            if f_count == 1:
                res += x
        return res
    else:
        return None

