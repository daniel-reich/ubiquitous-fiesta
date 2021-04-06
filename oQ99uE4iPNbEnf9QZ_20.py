
from functools import reduce
def no_perms_digits(n):
  if n<=1:
    return 1
  else:
    return len(str(reduce(lambda x, y: x*y, [x for x in range(1, n+1)])))

