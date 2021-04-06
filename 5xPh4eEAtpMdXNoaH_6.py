
from collections import Counter as cnt
def longest_palindrome(s):
  cs,odd,res = cnt(s),False,0
  for v in cs.values():
    if v&1:
      odd = True
      res += v-1
    else:
      res += v
  return res + odd

