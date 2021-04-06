
def fibonacci(n):
    n = n + 2
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    length = len(fib_list)
    return fib_list[length-1]

