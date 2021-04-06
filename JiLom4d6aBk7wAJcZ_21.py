
import math
def is_sastry(n):
  new_number = int(str(n) + str(n+1))
  if str(math.sqrt(new_number)).split('.')[1] != '0':
    return False
  else:
    return True

