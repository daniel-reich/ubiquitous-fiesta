
import math
def climb(stamina, obstacles):
    p = 0
    for i in range(1, len(obstacles)):
        cost = obstacles[i] - obstacles[i-1]
        if cost > 0:
            dp = math.ceil(cost) * 2
        else:
            dp = math.ceil(- cost)
        stamina = stamina - dp
        if stamina < 0:
            return p
        p += 1
    return p

