
import re
​
def count_ones(lst):
  s = str(lst)
  return len(re.findall(r'(1(, )?){2,}', s))

