
import math
def power_ranger(power, minimum, maximum):
    result = 0
    for i in range(math.ceil(minimum**(1/power)), math.ceil(maximum**(1/power))+1):
        if i**power >= minimum and i**power <= maximum:
            result+=1
    return result

