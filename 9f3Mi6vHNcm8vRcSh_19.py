
import math
​
def number_split(n):
    if n % 2 == 0:
        return [n // 2] * 2
    else:
        el1 = math.floor(n / 2)
        el2 = math.ceil(n / 2)
        return [el1, el2]

