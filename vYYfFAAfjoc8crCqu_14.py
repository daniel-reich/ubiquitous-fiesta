
def tree(h):
  return [' '*(h - x - 1) + '#'*(2*x + 1) + ' '*(h - x - 1) for x in range(h)]

