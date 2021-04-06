
import math
def combinations(k, n):
  return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

