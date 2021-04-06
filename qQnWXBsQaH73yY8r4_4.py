
import math
​
def kempner(n):
    for i in range(1,n+1):
      if math.factorial(i) % n == 0:
        return i

