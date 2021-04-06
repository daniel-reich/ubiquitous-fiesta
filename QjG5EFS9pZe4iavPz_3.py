
def fib(number):
    a, b = 0, 1
    for i in range(number):
        a, b = b, b + a
    return a

