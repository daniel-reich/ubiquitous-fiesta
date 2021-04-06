
import re
expr = re.compile(r'(\d+)\[([^\[\]]+)\]')
​
def string_builder(s):
  while True:
    m = expr.search(s)
    if not m:
      break
    count, substring = int(m.group(1)), m.group(2)
    s = s[:m.start()] +  substring * count + s[m.end():]
  return s

