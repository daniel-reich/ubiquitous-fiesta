
import re
def grab_number_sum(s):
  return sum(list(map(int,re.findall('\d+',s))))

