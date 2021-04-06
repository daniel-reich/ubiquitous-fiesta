
import re 
​
def longest_zero(s):
  st = sorted(re.findall(r'[0]+', s), key=len)
  return st[-1] if len(st) else ''

