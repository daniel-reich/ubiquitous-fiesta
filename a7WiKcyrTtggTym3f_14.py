
def lcm(a, b):
    if a > b:
        a, b = b, a
    for x in range(b, a * b + 1, b):
        if not x % a:
            return x

