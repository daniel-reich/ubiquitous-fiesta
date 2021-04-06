
def findall(src, c):
  res, s = [], 0
  while True:
    i = src.find(c, s)
    if i < 0:
      return res
    else:
      res.append(i)
      s = i + 1
​
def max_pairwise_dif(lst):
  p = [i2 - i1 for i1, i2 in zip(lst, lst[1:])]
  return max(p, default=0)
  
def max_separator(string):
  sstr = [(c, max_pairwise_dif(findall(string, c))) for c in set(string)]
  opt_len = max(sstr, key=lambda t: t[1])[1]
  if not opt_len:
    return []
  return list(sorted(t[0] for t in sstr if t[1] >= opt_len))

