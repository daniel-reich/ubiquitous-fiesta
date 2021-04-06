
import re
def grab_number_sum(s):
  return sum(map(int,re.findall('\d+',s)))

