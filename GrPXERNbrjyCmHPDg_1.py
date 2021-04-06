
def duplicate_count(txt):
  return len([c for c in set(txt) if txt.count(c)>1])

