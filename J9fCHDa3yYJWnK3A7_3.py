
def is_happy(n):
    if n in (1, 4):
        return n == 1
    return is_happy(sum([(int(x)**2) for x in str(n)]))

