
def same(a1, a2):
  a11 = list(dict.fromkeys(a1))
  a22 = list(dict.fromkeys(a2))
  return len(a11) == len(a22)

