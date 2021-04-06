
import math
def pascals_triangle(n):
  row = ""
  for k in range(0, n+1):
    num = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    row = row + str(num) + " "
  return row.rstrip()

