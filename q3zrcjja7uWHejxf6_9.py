
import re
​
def negative_sum(chars):
  return sum(map(int, re.findall('-\d+', chars)))

