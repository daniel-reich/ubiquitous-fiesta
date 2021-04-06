
def grouping(w):
  d = {}
  for t in sorted(w, key = lambda x: x.upper()):
    upper = sum(c.isupper() for c in t)
    if upper in d:
      d[upper].append(t)
    else:
      d[upper] = [t]
  return d

