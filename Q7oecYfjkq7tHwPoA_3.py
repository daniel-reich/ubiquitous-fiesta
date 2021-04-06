
import math
​
def climb(stamina, obstacles):
    cnt = 1
    for i in range(1, len(obstacles)):
        diff = obstacles[i] - obstacles[i-1]
        if diff > 0:
            # climbing up:
            d = math.ceil(diff)
            stamina -= 2 * d
        elif diff < 0:
            # climbing down
            d = -math.floor(diff)
            stamina -= d
        if stamina < 0:
            return cnt - 1
        elif stamina == 0:
            return cnt
        cnt += 1
    return cnt - 1

