
def newton_raphson(c):
    cprime = [c[0]*3, c[1]*2, c[2]]
    x = 0
    while True:
        xn = x - (c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]) / (cprime[0]*x**2 + cprime[1]*x + cprime[2])
        if round(x, 4) == round(xn, 4):
            break
        x = xn
​
    return round(x,3)

