
def dist(line, x, y):
    m = line[2:line.find('x')]
    line = line.replace('x', '*'+str(x))
    line = line.replace('y', '0')
    line += '-y'
    line = line.replace('y', str(y))
    return round(abs(eval(line[2:]))/((eval(m+'**2')+1)**0.5),2)

