
def is_isomorphic(s, t):
  if len(s) != len(t):
    return False
​
  for c in set(s):
    indices = [pos for pos, char in enumerate(s) if char == c]
    otherletter = t[indices[0]]
    indices2 = [pos for pos, char in enumerate(t) if char == otherletter]
    if indices != indices2:
      return False
  return True

