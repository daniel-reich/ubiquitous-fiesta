
import re
def score_it(s):
  lst = re.findall('\d+|\(+|\)+', s)
  res = 0
  d = 0
  for i in lst:
    if i.isdigit():
      res += int(i)*d
    elif '(' in i:
      d += len(i)
    elif ')' in i:
      d -= len(i)
  return res

