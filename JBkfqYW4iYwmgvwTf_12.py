
import math
​
def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, math.ceil(math.sqrt(num)+1)):
        if not num % i:
            return False
    return True

