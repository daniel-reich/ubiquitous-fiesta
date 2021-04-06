
import re
​
def count_number(lst):
  return len(re.findall('\d+\.\d+|\d+', str(lst)))

