
import re
​
def count_ones(lst):
  reg = re.compile(r'11+')
  return len(reg.findall(''.join(str(i) for i in lst)))

