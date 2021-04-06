
dx = 0.0001
steps = 20
x0 = 0
​
def f(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d
​
def f_prime(a, b, c, d, x):
    return 3 * a * x**2 + 2 * b * x + c
​
def newton_raphson(lst):
    a, b, c, d = lst
    x = x0
    for i in range(steps):
        x = x - f(a, b, c, d, x) / f_prime(a, b, c, d, x)
    return round(x, 3)

