
def simple_check(a, b):
    if a == b:
        return a
    elif a < b:
        a, b = b, a
    count = 0
    while b:
        if not a % b:
            count += 1
        a, b = a - 1, b - 1
    return count

