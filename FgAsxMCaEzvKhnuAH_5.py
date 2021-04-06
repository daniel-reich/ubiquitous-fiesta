
import re
def deep_sum(lst):
  count = 0
  for el in lst:
    if isinstance(el,list):
      count += deep_sum(el)
    else:
      count += sum(list(map(lambda x: int(x),re.findall(r'\-?\d+',el))))
  return count

