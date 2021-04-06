
def solve_for_exp(a, b):
    bob = 0
    while b != a:
        b = b / a
        bob += 1
    return bob+ 1

