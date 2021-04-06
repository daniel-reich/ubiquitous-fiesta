
import math
def vol_shell(r1, r2):
    result = 0
    if r1 >= r2:
        result = (4/3)*math.pi*(r1 ** 3 - r2 ** 3)
        return round(result, 3)
    if r1 <= r2:
        result = (4/3)*math.pi*(r2 ** 3 - r1 ** 3)
        return round(result, 3)

