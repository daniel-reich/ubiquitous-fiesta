
import re
def deep_sum(lst):
  els = flat(lst)
  return sum(part(el) for el in els)
  
def flat(lst):
  return sum([flat(e) if type(e)==list else [e] for e in lst], [])
  
def part(el):
  nums = re.findall(r'\-?\d+', el)
  return sum(int(num) for num in nums)

