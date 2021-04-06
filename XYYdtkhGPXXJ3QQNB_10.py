
import re
​
def num_in_str(lst):
  return [x for x in lst if re.match('.*\d', x)]

