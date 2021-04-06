
import math
def prime(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    elif num != 2 and num % 2 == 0:
        return False
    else:
        m = int(math.sqrt(num)) + 2
        for i in range(3,m,2):
            if num % i == 0:
                return False
        return True

