
def newton_raphson(c):
    x = 0
    derivative = '{}*x**2 + {}*x + {}'.format(c[0]*3,c[1]*2,c[2])
    function = '{}*x**3 + {}*x**2 + {}*x + {}'.format(c[0],c[1],c[2],c[3])
    for i in range(100):
        x = x - eval(function) / eval(derivative)
    return round(x, 3)

