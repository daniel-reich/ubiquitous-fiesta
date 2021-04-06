
def fib_fast(num):
    response = 0
    fib1 = 0
    fib2 = 1
    for x in range(1, num):
        response = fib1 + fib2
        fib1 = fib2
        fib2 = response
    return response

