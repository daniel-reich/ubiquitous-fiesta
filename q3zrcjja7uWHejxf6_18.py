
import re
def negative_sum(s):
  return sum(int(n) for n in re.findall(r'-\d+', s))

