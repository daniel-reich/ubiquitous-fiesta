
def divisible_by_b(a, b):
    x = max(a, b) + 1
    while x % b:
        x += 1
    return x

