
import math
def pascals_triangle(row):
  res = []
  for k in range(0, row+1):
    a = math.factorial(row)//math.factorial(row-k)//math.factorial(k)
    res.append(str(a))
  return " ".join(res)

