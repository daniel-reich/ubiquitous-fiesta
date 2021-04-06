
def get_coin_balances(lst1, lst2):
  p1, p2 = 3, 3
  for m1, m2 in zip(lst1, lst2):
    if (m1, m2) == ('share', 'share'):
      p1 += 2
      p2 += 2
    elif (m1, m2) == ('share', 'steal'):
      p1 -= 1
      p2 += 3
    elif (m1, m2) == ('steal', 'share'):
      p1 += 3
      p2 -= 1
  return [p1, p2]

