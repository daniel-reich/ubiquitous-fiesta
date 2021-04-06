
import math
def is_sastry(n):
  num=int(str(n)+str(n+1))
  i=int(math.sqrt(num))
  if num==i*i:
    return True
  else:
    return False

