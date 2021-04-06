
from collections import Counter
​
def max_occur(text):
  count = Counter(text).most_common()
  most = count[0][1]
  return [c[0] for c in count if c[1] == most] if most > 1 else 'No Repetition'

