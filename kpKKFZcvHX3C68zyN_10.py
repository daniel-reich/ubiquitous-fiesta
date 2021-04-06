
def swap_cards(n1, n2):
  a = min([int(i) for i in str(n1)])
  b = str(n1).replace(str(a), str(n2)[0])
  c = str(n2).replace(str(n2)[0], str(a))
  return int(b) > int(c)

