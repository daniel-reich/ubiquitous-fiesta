
def swap_cards(n1, n2):
  d1, d2 = [n1 // 10, n1 % 10], [n2 // 10, n2 % 10]
  i = int(d1[0] > d1[1])
  d1[i], d2[0] = d2[0], d1[i]
  return d1[0] * 10 + d1[1] > d2[0] * 10 + d2[1]

