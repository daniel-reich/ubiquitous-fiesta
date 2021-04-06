
def pattern(w):
  res,dic,x = [],{},0
  for c in w:
    if c not in dic:
      dic[c] = x
      x += 1      
    res.append(dic[c])
  return res
      
def is_isomorphic(s, t):
  return pattern(s) == pattern(t)

