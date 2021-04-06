
import math
​
def climb(stamina, obstacles):
    tot = 0
    steps = [obstacles[i+1] - obstacles[i] for i in range(len(obstacles) - 1)]
    cost = [2 * math.ceil(i) if i >= 0 else abs(math.floor(i)) for i in steps]
    for i in cost:
        stamina -= i
        if stamina >= 0:
            tot += 1
        else:
            break
    return tot

