
import re
​
def score_it(s):
  matches = re.finditer(r'\d+', s)
  count = result = prev_end = 0
  for m in matches:
    slice = s[prev_end : m.start()]
    count += slice.count('(') - slice.count(')')
    result += count * int(s[m.start() : m.end()])
    prev_end = m.end()
  return result

