
import re
def find_longest(s):
  pos = s.find(' ')
  sub = (s[0: pos] if pos >= 0 else s).lower()
  sub = re.search(r'[a-z]+', sub).group(0)
  if pos < 0:
    return sub
  else:
    sub_next = find_longest(s[pos+1:])
    return sub if len(sub) > len(sub_next) else sub_next

