
def double_swap(txt, c1, c2):
  d={c1:c2,c2:c1}
  return ''.join([i if i!=c1 and i!=c2 else d[i] for i in txt])

