
import math
def shortestDistance(txt):
    txt = txt.replace(",", " ").split()
    x1 = float(txt[0])
    y1 = float(txt[1])
​
    x2 = float(txt[2])
    y2 = float(txt[3])
    
    return round(math.sqrt(((x2 - x1)**2)+((y2 - y1)**2)), 2)

