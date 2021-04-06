
import re
def grab_number_sum(s):
  lst = re.findall('\d+', s)
  return sum([int(i) for i in lst])

