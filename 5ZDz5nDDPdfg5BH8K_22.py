
import math
​
def only_5_and_3(n):
    if math.sqrt(n) == 3 or n % 5 == 0:
        return True
    else:
        n2 = 3
        while n2 < n:
            n2 *= 3
        n2 /= 3
​
        for _ in range(int(n2 / 3)):
            n3 = n2
            while n3 < n:
                n3 += 5
                if n3 == n:
                    return True
            n2 /= 3
            if n2 == 1:
                n2 = 0
​
        return False

