
import math
​
def kempner(n):
    for i in range(1,1000):
        f=math.factorial(i)
        if f%n==0:
            return i 
        else:
            pass

