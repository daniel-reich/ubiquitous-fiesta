
def is_isomorphic(s, t):
  if len(s) != len(t):
    return False
  mapping = {}
  for c1, c2 in zip(s, t):
    if c1 in mapping:
      if c2 != mapping[c1]:
        return False
    else:
      if c2 in mapping.values():
        return False
      mapping[c1] = c2
  return True

