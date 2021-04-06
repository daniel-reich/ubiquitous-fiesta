
def tree(h):
  if h == 0:
    return []
  return [' '*(h - n) + '#'*(2*n - 1) + ' '*(h - n) for n in range(1,h+1)]

