
from collections import Counter
​
def max_occur(text):
  c = Counter(text).items()
  ans = sorted([i[0] for i in c if i[1] == max([x[1] for x in c])])
  return 'No Repetition' if max([x[1] for x in c]) == 1 else ans

