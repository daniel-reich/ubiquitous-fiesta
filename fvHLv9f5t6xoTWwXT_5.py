
import re
def grab_number_sum(s):
  return sum(int(x) for x in re.findall('\d+',s))

