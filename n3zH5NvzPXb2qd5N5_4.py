
import math
def how_mega_is_it(n):
    x = abs(int(n))
    if x < 100:
        return "not a mega milestone"
    elif len(str(x))==3:
        return "MEGA milestone"
    else:
        a = len(str(x)[:-2])
        return "MEGA "*a+"milestone"

