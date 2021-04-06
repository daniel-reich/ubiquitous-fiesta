
def dist(line,x0,y0):
    '''
    Returns the shortest distance from line to the point at x0, y0
    '''
    # Uses Equation abs(c+ax0-y0))/sqrt(1 + a*a)
    c = eval(line[line.index('x')+1:])
    a = eval(line[line.index('=')+1:line.index('x')])
​
    return round(abs(c+a*x0-y0)/(1 + a*a)**0.5, 2)

