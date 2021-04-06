
import re
​
def negative_sum(chars):
  m = re.findall('([-]+[0-9]{1,})', chars)
  m = [int(el) for el in m]
  return sum(m)

