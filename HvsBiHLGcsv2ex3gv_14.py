
def shortestDistance(txt):
    p = txt.split(',')
    p1 = int(p[0]), int(p[1])
    p2 = int(p[2]), int(p[3])
    a, b = abs(p1[0]-p2[0])**2, abs(p1[1]-p2[1])**2
    c = (a+b)**0.5
    ans = round(c, 2)
    return ans

