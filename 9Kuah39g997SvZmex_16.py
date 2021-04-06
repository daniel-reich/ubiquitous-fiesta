
from collections import Counter
def common_last_vowel(txt):
  res = []
  for w in txt.lower().split():
    v = [c for c in w if c in 'aeiou']
    res.append(v[-1])
  return Counter(res).most_common(1)[0][0]

