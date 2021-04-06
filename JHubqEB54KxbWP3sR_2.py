
import math
def dist(line, x, y):
    b = 1
    l = line.split("x")
    c = -eval(l[1])
​
​
    for i in l:
        if "y=" in i:
            a = -eval(i[2::])
​
    k = abs((a * x) + (b * y) + (c))
    g = (math.sqrt((a * a) + (b * b)))
    return round(k / g, 2)

