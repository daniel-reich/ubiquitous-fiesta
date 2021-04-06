
import math
def cal(depth):
    H = depth
    T = 0
    while H > 150:
        H = H - 150
        T = T + 30
        T = T + 10
        H = H + 30
    if H > 0:
        T = T + H/5
    return math.ceil(T)

