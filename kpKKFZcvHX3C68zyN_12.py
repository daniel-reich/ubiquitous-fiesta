
def swap_cards(n1, n2):
  d1,u1 = [u for u in str(n1)]
  d2,u2 = [u for u in str(n2)]
  if d1 <= u1:
    return [d2,u1] > [d1,u2]
  else:
    return [d1,d2] > [u1,u2]

