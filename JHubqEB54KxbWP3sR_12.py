
def dist(line,x,y):
    from math import sqrt
    a=-eval(line[line.index("=")+1:line.index("x")])
    b=1
    c=-eval(line[line.index("x")+1:])
    return round((abs(a*x+b*y+c))/(sqrt(a*a+b*b)),2)

