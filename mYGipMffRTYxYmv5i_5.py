
def simple_equation(a, b, c):
    myans = ''
    if a+b == c:
        myans = str(a)+'+'+str(b)+'='+str(c)
        return myans
    if a-b == c:
        myans = str(a)+'-'+str(b)+'='+str(c)
        return myans
    if a*b == c:
        myans = str(a)+'*'+str(b)+'='+str(c)
        return myans
    if a//b == c:
        myans = str(a)+'/'+str(b)+'='+str(c)
        return myans
​
    return myans

