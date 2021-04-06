
from collections import Counter
def isValid(s):
  if meh(s): return 'YES'
  for i in range(len(s)):
    if meh(s[:i]+s[i+1:]):
      return 'YES'
  return 'NO'
​
meh = lambda s: len(set(Counter(s).values())) == 1

