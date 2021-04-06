
def fibonacci(num):
    if num < 2:
        return 1
    a, b = 1, 1
    idx = 1
    while idx != num:
        a, b = b, a + b
        idx += 1
    return b

