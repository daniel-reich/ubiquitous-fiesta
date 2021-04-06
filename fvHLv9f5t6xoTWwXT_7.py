
import re
def grab_number_sum(s):
  return eval(re.sub(r'[a-z]*(\d+)[a-z]*',lambda i:'+'+i.group(1),s)[1:])

