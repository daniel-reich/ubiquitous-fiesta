
from string import ascii_uppercase as au
def title_to_number(s):
  dic = dict(zip(au,range(1,27)))
  res = 0
  while s:
    x,s = s[:1],s[1:]
    res += dic[x]
    res *= 26 if s else 1
  return res

