
def swap_cards(n1, n2):
  a,b = list(str(n1))
  c,d = list(str(n2))
  if a<=b:
    a,c = c,a
  else:
    b,c = c,b
  n1 = int(str(a)+str(b))
  n2 = int(str(c)+str(d))
  return n1>n2

