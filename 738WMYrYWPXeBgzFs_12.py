
from collections import Counter
​
def is_valid_(txt):
  counter = Counter(txt)
  same = True
  pre_value = counter.get(txt[0])
  for key, value in counter.items():
    if value == pre_value:
      value = pre_value
      continue
    return False
  return same
​
​
def is_valid(txt):
  check = is_valid_(txt)
  if check==False:
    counter = Counter(txt)
    for key, value in counter.items():
      if value == min(counter.values()):
        txt_ = txt[:txt.index(key)] + txt[txt.index(key)+1:]
    check = is_valid_(txt_)
​
    if check==False:
      for key, value in counter.items():
        if value == max(counter.values()):
          txt_ = txt[:txt.index(key)] + txt[txt.index(key)+1:]
      check = is_valid_(txt_)
  if check:
    return "YES"
  return "NO"

