
def newton_raphson(c):
    count=0;x=0
    while count<20:
        f=c[0]*x**3+c[1]*x**2+c[2]*x+c[3]
        fp=3*c[0]*x**2+2*c[1]*x+c[2]
        x=x-f/fp
        count+=1
    return round(x,3)

