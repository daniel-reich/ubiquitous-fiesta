
import re
def grab_number_sum(s):
  return sum(0 if not x else int(x) for x in re.split('[A-Za-z]+', s))

