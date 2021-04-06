
import random
import math
def is_prime(n):
    return fermat_check(n,3)
​
def fermat_check(num, count):
    for _ in range(count):
        random_val = int(random.randint(1, num-1))
        if pow(random_val, num-1, num) != 1:
            return False
    return True

