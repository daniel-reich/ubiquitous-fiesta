
def grouping(w):
  g = {}
  for i in w:
      upp = sum(1 for c in i if c.isupper())
      g.setdefault(upp,[]).append(i)
      g[upp].sort(key = str.lower)
  return(dict((key, g[key]) for key in sorted(g)))

