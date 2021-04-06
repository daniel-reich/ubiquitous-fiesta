
import math
def pascals_triangle(n):
  triangle = []
  for row in range(n):
    new_row = []
    for k in range(row+1):
      new_row.append(math.factorial(row)//(math.factorial(k)*math.factorial(row-k)))
    triangle += new_row
  return triangle

