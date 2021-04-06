
import re
​
def is_authentic_skewer(s):
  c, v = '[^AEIOU]', '[AEIOU]'
  return bool(re.search(r'^{0}(\W+)({1}\1{0}\1)*{1}\1{0}$'.format(c, v), s))

