
def newton_raphson(const):
    c3,c2,c1,c0 = const
    x = 0
    func = lambda x: c3*x**3 + c2*x**2 + c1*x + c0
    deriv = lambda x: c3*3*x**2 + c2*2*x +c1
    for i in range(20):
        x = x - func(x)/deriv(x)
        
    return round(x, 3)

