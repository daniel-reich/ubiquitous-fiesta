
def newton_raphson(c, x0 = 0, i = 0):
    fx = lambda x: c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]
    dfx = lambda x: 3*c[0]*x**2 + 2*c[1]*x + c[2]
​
    x1 = x0 - fx(x0) / dfx(x0)
    return round(x1, 3) if abs(x1-x0) < 0.00001 else newton_raphson(c, x1, i+1)

