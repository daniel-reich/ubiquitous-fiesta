
import math
def shortestDistance(txt):
    x1,y1,x2,y2=txt.split(',')
    return round(math.sqrt( (int(x1)-int(x2))**2+(int(y1)-int(y2))**2 ),2)

