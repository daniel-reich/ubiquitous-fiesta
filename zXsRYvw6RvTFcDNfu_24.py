
def prime_factors(num):
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return res
​
​
def ruth_aaron_type(m, n):
    m_factors, n_factors = prime_factors(m), prime_factors(n)
    def_1, def_2 = False, False
    if sum(set(m_factors)) == sum(set(n_factors)):
        def_1 = True
    if sum(m_factors) == sum(n_factors):
        def_2 = True
    if def_1 & def_2:
        return 3
    elif def_1:
        return 1
    elif def_2:
        return 2
    else:
        return 0
​
​
def ruth_aaron(n):
    ruth = ruth_aaron_type(n, n + 1)
    aaron = ruth_aaron_type(n - 1, n)
    if ruth:
        return ['Ruth', ruth]
    if aaron:
        return ['Aaron', aaron]
    return False

