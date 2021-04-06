
import re
def flatten(lst):
  r = []
  for itm in lst:
    if isinstance(itm, list):
      r.extend(flatten(itm))
    else:
      r.append(itm)
  return r
​
def deep_sum(lst):
  s = 'X'.join(flatten(lst))
  nums = re.findall(r'-?\d+', s)
  return sum(int(n) for n in nums)

