
def grouping(w):
  d,l={},[len([h for h in list(i) if h.isupper()]) for i in w]
  [d.update({i:[h]}) if i not in d else d[i].append(h) for i,h in zip(l,w)]
  return {i:sorted(h,key=str.lower) for i,h in sorted(d.items())}

