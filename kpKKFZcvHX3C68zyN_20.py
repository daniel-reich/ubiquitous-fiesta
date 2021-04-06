
def swap_cards(n1, n2):
  p1 = [i for i in str(n1)]
  p2 = [i for i in str(n2)]
  val, idx = min((val, idx) for (idx, val) in enumerate(p1))
  p1[idx], p2[0] = p2[0], p1[idx]
  return p1 > p2

