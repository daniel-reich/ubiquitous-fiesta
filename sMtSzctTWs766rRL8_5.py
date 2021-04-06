
import math
​
def magnitude(lst):
  if lst == []:
    return 0
  else:
    square_sum = 0
    for i in lst:
      square_sum += i ** 2
    dist = math.sqrt(square_sum)
    return dist

