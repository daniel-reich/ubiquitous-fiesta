
def duplicate_count(txt):
  seen = set()
  return len(set([c for c in txt if (c in seen or seen.add(c))]))

