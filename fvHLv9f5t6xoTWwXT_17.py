
import re
​
def grab_number_sum(s):
  return sum(int(num) for num in re.findall("[0-9]+", s))

