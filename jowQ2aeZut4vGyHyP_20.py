
import math
def convert(slope):
    angleFromX = abs(round(math.degrees(math.atan(slope))))
    
    if slope >= 0:
        return 90 - angleFromX
    else:
        return 90 + angleFromX

