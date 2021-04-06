
import re
def grab_number_sum(s):
  test = filter(None, re.findall(r'\d*', s))
  return sum([int(x) for x in test])

