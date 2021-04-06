
from collections import Counter
​
def common_last_vowel(txt):
  v = [[c for c in word if c in "aeiou"][-1] for word in txt.lower().split()]
  return Counter(v).most_common()[0][0]

