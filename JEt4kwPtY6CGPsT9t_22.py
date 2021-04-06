
def mathematical(exp, numbers):
    x = []
    for i in numbers : 
        c = int(exp[-1])
        a = i
        b = exp[6]
        if b == '+':
            d= a+c 
            x+= ["f({})={}".format(a,d)]
        elif b == '-':
            d= a-c
            x+= ["f({})={}".format(a,d)]
        elif b == 'x':
            d= a*c
            x+= ["f({})={}".format(a,d)]
        elif b == '/':
            d =int(a/c)
            x+= ["f({})={}".format(a,d)]
        elif b == '^':
            d = a**2
            x+= ["f({})={}".format(a,d)]
    return x

