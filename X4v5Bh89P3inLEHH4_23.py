
import math
def spin_around(lst):
  count = 0
  for i in lst:
    if i == 'right':
      count += 90
    else:
      count -= 90
  return count // 360 if count > 0 else abs(math.ceil(count / 360))

