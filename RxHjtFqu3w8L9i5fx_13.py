
import math
def bell(n):
  resolution = 100
  return round((1/math.e) * sum([(k**n)/math.factorial(k) for k in range(resolution)]))

