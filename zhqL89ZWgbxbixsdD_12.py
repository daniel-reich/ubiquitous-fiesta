
import math
​
def is_exact(n, i=1):
  return [n, i] if math.factorial(i) == n \
    else is_exact(n, i+1) if math.factorial(i) < n else "Not exact!"

