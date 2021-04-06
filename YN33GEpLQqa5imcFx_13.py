
import math
​
def pascals_triangle(row):
    return ' '.join([str(int(math.factorial(row)/(math.factorial(column) * math.factorial((row-column))))) for column in range(0, row+1)])

