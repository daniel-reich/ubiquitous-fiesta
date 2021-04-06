
from collections import Counter
def is_valid(txt):
  freq = Counter(txt)
  freq_0 = freq[txt[0]]
  diff = 0
  for f in freq.values():
    d = abs(f - freq_0)
    if d > 1:
      return "NO"
    elif d == 1:
      diff += 1
  return "YES" if diff in (0, 1, len(freq)-1) else "NO"

