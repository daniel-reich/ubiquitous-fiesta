
def duplicate_count(txt):
  return sum([1 for c in set(txt) if txt.count(c) > 1 ])

