
import math
def digits_count(num):
    if num==0:
        return 1
    return math.floor(math.log(abs(num),10)+1)

