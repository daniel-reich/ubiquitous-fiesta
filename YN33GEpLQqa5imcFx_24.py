
import math
​
def pascals_triangle(n):
    triangle = '1'
    for x in range(1, n+1):
        triangle += ' ' + str(int(math.factorial(n)/ (math.factorial(x) * math.factorial(n-x))))
    return triangle

