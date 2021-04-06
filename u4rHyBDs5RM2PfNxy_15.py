
import re
def count_ones(lst):
  txt = ''.join([str(i) for i in lst])
  regex = '[1]{2,}'
  return len(re.findall(regex,txt))

