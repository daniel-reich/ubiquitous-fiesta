
def is_isomorphic(s, t):
  tran = {}
  for i,c in enumerate(t):
    if c in tran:
      if s[i] != tran[c]:
        return False
    else:
      tran[c] = s[i]
  return True

