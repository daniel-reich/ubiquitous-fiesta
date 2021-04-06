
def fibFast(num):
    a, b = 0, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return b

