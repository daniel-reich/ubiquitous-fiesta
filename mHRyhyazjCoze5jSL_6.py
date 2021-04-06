
def double_swap(txt, c1, c2):
  s1 = c1+c2
  s2 = c2+c1
  trans = txt.maketrans(s1,s2)
  return txt.translate(trans)

