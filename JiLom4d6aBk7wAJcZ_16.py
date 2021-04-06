
import math
def is_sastry(n):
    a = int(str(n)+str(n+1))
    if a**.5 == math.floor(a**.5):
        return True
    return False

