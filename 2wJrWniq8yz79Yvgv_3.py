
def is_narcissistic(n):
    return n == sum([int(a)**len(str(n)) for a in str(n)])

