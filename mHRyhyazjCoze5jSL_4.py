
def double_swap(txt, c1, c2):
  return c2.join(u.replace(c2,c1) for u in txt.split(c1))

