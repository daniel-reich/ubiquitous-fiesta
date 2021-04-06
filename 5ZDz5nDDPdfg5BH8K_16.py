
import math
​
def only_5_and_3(n):
  if n % 5 == 0:
    return True
  else:
    threes = list(map(lambda x: pow(3,x),range(1,math.ceil(math.log(n,3)))))
    fives = list(map(lambda x: n - x,threes))
    lst = list(filter(lambda x: x % 5 == 0,fives))
    return len(lst) > 0

