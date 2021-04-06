
import re
​
def left_digit(num):
  x = re.search("\d+", num)
  return int(x.group(0))

