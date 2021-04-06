
import re
​
def final_result(lst):
  txt = ''.join(lst)
  while re.search(r'(\w)\1', txt):
    m = re.search(r'(\w)\1+', txt).group(0)
    txt = re.sub(m, '', txt)
  return list(txt)

