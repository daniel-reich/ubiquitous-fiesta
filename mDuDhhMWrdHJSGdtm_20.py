
def is_exactly_three(n):
    sqrt = round(n**(1/2))
    return sqrt >= 2 and sqrt**2 == n and all(n % i for i in range(2,sqrt//2+1))

