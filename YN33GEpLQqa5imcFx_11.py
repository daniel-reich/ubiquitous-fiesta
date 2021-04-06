
import math
​
def pascals_triangle(row):
    n = row
    row_elements = '1'
    for k in range(1,row):
        row_elements += ' ' + str(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))
    return row_elements+' 1'

