
import math
​
def Log2(x):
  if x == 0: return false;
  else: return math.log10(x) / math.log10(2)
  
def power_of_two(num):
  return math.ceil(Log2(num)) == math.floor(Log2(num))

