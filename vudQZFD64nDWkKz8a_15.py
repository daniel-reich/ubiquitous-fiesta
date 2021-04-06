
import re
​
def grant_the_hint(txt):
  s = re.sub(r"\S", "_", txt)
  res = [s]
​
  while "_" in s:
    s = re.sub(r"(?<!_)_", lambda m: txt[m.start()], s)
    res.append(s)
​
  return res

