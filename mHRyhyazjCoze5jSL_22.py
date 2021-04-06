
def double_swap(txt, c1, c2):
  t = txt.translate(str.maketrans({c1: c2, c2: c1}))
  return t

