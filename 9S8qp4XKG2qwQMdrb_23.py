
def ways_to_climb(n):
    def fib(x):
        if x <= 1:
            return x
        return fib(x - 1) + fib(x - 2)
    return fib(n + 1)

