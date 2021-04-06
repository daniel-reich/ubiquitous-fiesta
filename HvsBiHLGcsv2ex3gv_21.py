
def shortestDistance(txt):
    numbers=[int(a) for a in txt.split(',')]
    x1,y1,x2,y2 = numbers
    import math
    substract=(x2-x1)**2+(y2-y1)**2
    dist = math.sqrt(substract)
    return round(dist,2)

