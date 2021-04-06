
def shortestDistance(txt):
    x1, y1, x2, y2 = [int(n) for n in txt.split(',')]
    d = ((x2 - x1)**2 + (y2 - y1)**2)**.5
    return round(d, 2)

