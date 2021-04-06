
def dist(line, x, y):
    p=line.find('x')
    a=eval(line[2:p])
    c=eval(line[p+1:])
    return round(abs(a*x-y+c)/(a**2+1)**.5,2)

