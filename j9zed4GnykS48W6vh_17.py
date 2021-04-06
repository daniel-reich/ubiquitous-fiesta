
import math
def digits(n):
  t = 0
  for i in range(len(str(n))):
    t += n-int(math.pow(10,i))
  return t

