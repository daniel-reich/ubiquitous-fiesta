
import re
def grab_number_sum(n):
  return sum([int(i) for i in re.findall(r'-?\d+\.?\d*', n)])

