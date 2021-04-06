
from collections import Counter
​
def get_notes_distribution(students):
  return Counter(n for s in students for n in s["notes"] if 1 <= n <= 5)

