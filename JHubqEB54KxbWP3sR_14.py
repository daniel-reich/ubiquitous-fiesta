
def dist(line, x, y):
    ix = line.index('x')
    m, c = eval(line[2:ix]), eval(line[ix+1:])
    xi = (y * m + x - c * m) / (m * m + 1)
    yi = xi * m + c
    return round(((x - xi)**2 + (y - yi)**2)**0.5, 2)

