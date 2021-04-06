
def get_coin_balances(l1, l2):
  x = -l1.count('share') + (l2.count('share') * 3) + 3
  y = -l2.count('share') + (l1.count('share') * 3) + 3
  return [x,y]

