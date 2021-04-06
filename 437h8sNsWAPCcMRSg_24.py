
def product_of_primes(num):
    from functools import reduce
    from itertools import permutations
    primes_list = lambda N: list(reduce((lambda r, x: r - set(range(x ** 2, N, x)) if (x in r) else r),
                                        range(2, N), set(range(2, N))))
​
    perm = permutations(sorted(primes_list(round(num - 1))), 2)
​
    h = [True for i in perm if i[0] * i[1] == num or i[0] ** 2 == num or i[1] ** 2 == num]
    return True if True in h else False

