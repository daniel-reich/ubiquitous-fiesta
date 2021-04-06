
def duplicate_count(txt):
  from collections import Counter
  counted = Counter(txt)
  return len([counted[k] for k in counted if k.isalnum() and counted[k] > 1])

