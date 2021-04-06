
def find_shortest_words(txt):
  res=[w for w in ''.join(c for c in txt if c.isalnum() or c==' ').lower().split() if w.isalpha()]
  return sorted([w for w in res if len(w)==len(min(res,key=len))])

