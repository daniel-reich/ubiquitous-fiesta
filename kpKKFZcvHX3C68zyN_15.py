
def swap_cards(n1, n2):
  p, o = list(str(n1)), list(str(n2))
  i = p[0] > p[1]
  p[i], o[0] = o[0], p[i]
  return p > o

