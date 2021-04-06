
def grouping(w):
  d = {}
  w = sorted(w, key=str.casefold)
  for word in w:
    count = 0
    for c in word:
      if c.isupper(): count += 1
    if count not in d:
      d[count] = []
    d[count].append(word)
  return d

