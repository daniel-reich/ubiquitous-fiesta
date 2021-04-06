
def grouping(w):
  group = {}
  for word in w:
    n = sum(c.isupper() for c in word)
    if n not in group:
      group[n] = []
    group[n].append(word)
  return {k:sorted(v, key = lexi) for k,v in group.items()}
  
def lexi(w):
  return [ord(c) for c in w.lower()]

