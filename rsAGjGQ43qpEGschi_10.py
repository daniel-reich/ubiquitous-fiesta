
def newton_raphson(c):
    def polynomial(x):
        return c[0] * x ** 3 + c[1] * x ** 2 + c[2] * x + c[3]
​
    def derivative_polynomial(x):
        return 3 * c[0] * x ** 2 + 2 * c[1] * x + c[2]
​
    arg = 0
    while abs(polynomial(arg)) > 0.001:
        arg -= polynomial(arg) / derivative_polynomial(arg)
    return round(arg, 3)

