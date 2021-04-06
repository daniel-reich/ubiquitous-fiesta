
import math
def is_factorial(n):
    lst=[]
    for i in range(0,n+1):
         lst.append(math.factorial(i))
    return True if n in lst else False

