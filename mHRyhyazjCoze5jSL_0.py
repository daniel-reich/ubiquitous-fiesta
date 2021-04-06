
def double_swap(txt, c1, c2):
  return txt.translate(str.maketrans(c1+c2, c2+c1))

