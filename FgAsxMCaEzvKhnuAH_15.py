
import re
def deep_sum(lst):
  s=str(lst)
  p=r'\-?[0-9]+'
  return sum([int(x) for x in re.findall(p,s)])

