
import re
def grab_number_sum(s):
  return sum(int(i) for i in re.findall('\d+',s))

