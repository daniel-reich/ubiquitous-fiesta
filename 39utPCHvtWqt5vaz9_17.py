
def direction(lst):
  import re
  s = ''
  ans = []
  for l in lst:
    s = re.sub(r'e',r'w',l)
    s = re.sub(r'a',r'e',s)
    s = re.sub(r'E',r'W',s)
    s = re.sub(r'A',r'E',s)
    ans.append(s)
  return ans

