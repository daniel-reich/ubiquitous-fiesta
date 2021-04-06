
import re
from itertools import product
​
def unravel(txt):
  groups = [i.strip('[]').split('|') for i in re.findall(r'\[[[^\[\]]|\|]+\]|[^\[\]]+', txt)]
  return sorted(''.join(i) for i in product(*groups))

