
from collections import Counter
def missing_alphabets(txt):
  al = 'abcdefghijklmnopqrstuvwxyz'
  cnt = Counter(txt)
  M = max(cnt.values())
  return ''.join(l*(M-cnt[l]) for l in al)

