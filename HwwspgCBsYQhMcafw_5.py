
def super_digit(n, k, repeat=True):
    if repeat:
        n *= k
        repeat = False
    if len(n) == 1:
        return int(n)
    n = sum(int(i) for i in n)
    return super_digit(str(n), k, repeat)

