
import math
​
# gravity acceleration from example in specs:
g = 2.0 * 9.0 / 3.0**2
​
def bug_jump(height, time):
    time /= 1000.
    v = math.sqrt(2.0 * height * g)
    t_top = v / g
    if time >= 2 * t_top:
        return [0, None]
    y = round(abs(time**2 - time * 2 * t_top), 2)
    if time <= t_top:
        return [y, "up"]
    else:
        return [y, "down"]

