
def duplicate_count(txt):
  return sum(txt.count(x) > 1 for x in set(txt))

