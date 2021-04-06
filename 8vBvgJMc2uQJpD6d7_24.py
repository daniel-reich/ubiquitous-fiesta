
import math
import numpy as np
def prime_factors(n):
    lst = []
    while n % 2 == 0:
        n = n // 2
        lst.append(2)
    while True:
        sqrt_num = math.sqrt(n)
        for num in np.arange(3, sqrt_num + 1, 2):
            while n % num == 0:
                print(num)
                n = n // num
                lst.append(int(num))
        if n != 1:
            lst.append(int(n))
        break
    return lst

