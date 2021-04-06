
import re
​
def count_same_ends(txt):
  txt = re.sub(r'\W+', ' ', txt.lower())
  s = 0
  for i in txt.split(' '):
    if len(i) > 1 and i[0] == i[-1]:
      s += 1
  return s

