
import math
def bug_jump(height, time):
    midpoint =math.sqrt(height)
    time = time/1000
    if time > 2*midpoint:
        return [0,None]
    newheight = -(time - midpoint)**2 + height
    newheight = round(newheight,2)
    if time < midpoint:
        return [newheight, "up"]
    if time == 0 or time == 3 :
        return [newheight, None]    
    return [newheight , 'down']

