
def digit_count(n):
    n = str(n)
    return int(''.join(str(n.count(x)) for x in n))

