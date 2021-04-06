
def longest_zero(s):
  import re
  lst = re.findall(r'0+', s)
  return sorted(lst, key = len, reverse = True)[0] if len(lst) else ''

