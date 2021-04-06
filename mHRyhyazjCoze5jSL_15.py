
def double_swap(txt, c1, c2):
  return ''.join(c1 if c == c2 else c2 if c == c1 else c for c in txt)

