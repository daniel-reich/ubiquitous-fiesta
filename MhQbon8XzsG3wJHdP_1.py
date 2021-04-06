
def solve_for_exp(a, b):
    cnt = 0
    while b != a:
        b = b / a
        cnt += 1
    return cnt + 1

