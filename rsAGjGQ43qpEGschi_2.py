
def newton_raphson(c, x=0):
    for _ in range(20):
        polynomial = c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]
        derivative = 3*c[0]*x**2 + 2*c[1]*x + c[2]
        x -= polynomial/derivative
    return round(x, 3)

