
def is_isomorphic(s, t):
  mappings = {}
  for i, j in zip(s, t):
    if i not in mappings.keys():
      if j in mappings.values():
        return False
      else:
        mappings[i] = j
    elif mappings[i] != j:
      return False
  return True

