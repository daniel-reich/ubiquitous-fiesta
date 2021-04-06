
def grouping(words):
  res = {}
​
  for w in words:
    n_caps = sum(1 for ch in w if ch.isupper())
    if n_caps in res.keys():
      res[n_caps] += [w]
    else:
      res[n_caps] = [w]
​
  for item in res:
    res[item] = sorted(res[item],key=lambda x: (x.lower(),-len(x)))
  return res

