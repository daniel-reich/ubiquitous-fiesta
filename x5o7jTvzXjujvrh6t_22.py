
def i_sqrt(n):
  import math
  count = 0
  if n<0:
    return 'invalid'
  while n>=2:
    n = math.sqrt(n)
    count +=1
  return count

