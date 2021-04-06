
import math
def triangle(perimeter,area):
    triangles = []
    for a in range(1,math.floor(perimeter/3)+1):
        for b in range(a,math.floor((perimeter-a)/2)+1):
            c = perimeter - a - b
            s = perimeter/2
            if (s*(s-a)*(s-b)*(s-c) >= 0):
                if abs(math.sqrt(s*(s-a)*(s-b)*(s-c)) - area) < 0.0001:
                    triangles.append([a,b,c])
    return triangles

