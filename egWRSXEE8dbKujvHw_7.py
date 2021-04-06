
import math
def is_circle_collision(c1, c2):
    x=(c1[1]-c2[1])*(c1[1]-c2[1])
    y=(c1[2]-c2[2])*(c1[2]-c2[2])
    z=math.sqrt(x+y)
    if z<c1[0]+c2[0]:
        return True
    else:
        return False

