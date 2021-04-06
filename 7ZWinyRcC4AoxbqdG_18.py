
def fibo(n):
    a, b = 0, 1
    fibonacci = []
    for i in range(n+1):
        a, b = b, a+b
        fibonacci.append(a)
    return fibonacci[n-1]

