
import math
​
def vol_shell(r1, r2):
    V = (4/3)*math.pi*(r1**3 - r2**3)
    return round(abs(V), 3)

