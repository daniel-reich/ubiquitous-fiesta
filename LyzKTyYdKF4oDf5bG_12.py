
import re
​
def find_longest(s, longest = '', i = 0):
  txt = s.lower().split()
  if i == len(txt):
    return longest
  t = re.sub(r'[^a-z]', '', txt[i].replace("'s", ''))
  longest = t if len(t) > len(longest) else longest
  return find_longest(s, longest, i + 1)

