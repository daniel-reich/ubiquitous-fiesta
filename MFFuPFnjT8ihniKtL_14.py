
import math
def bug_jump(height, time):
    equation = lambda time: -(time-math.sqrt(height))**2+height
    vertex_time = math.sqrt(height)
    pos = round(equation(time/1000), 2)
    if pos < 0:
        return [0, None]
    d = "up" if time/1000 < vertex_time else "down"
    return [pos, d]

