
from functools import reduce
def mystery_func(num):
  return reduce(lambda x,y:int(x)*int(y),str(num))

