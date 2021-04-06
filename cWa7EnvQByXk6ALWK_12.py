
def golden_ratio():
    one_100_digits = 10**99
    fib1 = fibo(300) * one_100_digits
    fib2 = fibo(299)
    fib_str = str(fib1//fib2)
    fib_str = fib_str[0:1] + '.' + fib_str[1:]
    return fib_str                
​
def fibo(n):
    a, b = 0,1
    for x in range (n-1):
        a, b = b, a+b
    return b

