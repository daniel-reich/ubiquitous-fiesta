
def fibonacci(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return b

