
import re
def grab_number_sum(s):
  
  pattern = '[0-9]+'
  return eval('+'.join(re.findall(pattern,s)))

