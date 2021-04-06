
def solver(eq):
    y=[]
    eq=eq.replace('=','==')
    for i in range(-10,10):
        x=i
        if eval(eq):
            y.append(float(i))
    if len(y)==0:
        return "Infinite solutions"
    return y[0]

