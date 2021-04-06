
import math
def line_length(dot1, dot2):
    x1,y1 = dot1
    x2,y2 = dot2
    x = abs(x2-x1)
    y = abs(y2-y1)
    return round(math.sqrt(x**2 + y**2),2)

