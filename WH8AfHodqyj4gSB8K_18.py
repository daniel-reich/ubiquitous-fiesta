
import re
​
def is_authentic_skewer(s):
  C, V = '[B-DF-HJ-NP-TV-Z]', '[AEIOU]'
  return bool(re.match(r'{}(-+){}(\1{}\1{})*\1{}$'.format(C, V, C, V, C), s))

