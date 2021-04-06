
import re
def count_same_ends(txt):
  txt = re.sub(r'[^\w\s]','',txt).split()
  count = 0
  for n in txt:
    if n[0].lower() == n[-1].lower() and len(n) > 1:
      count += 1
  return count

