
from collections import Counter
def count_repetitions(lst):
  return dict(Counter(lst).most_common())

