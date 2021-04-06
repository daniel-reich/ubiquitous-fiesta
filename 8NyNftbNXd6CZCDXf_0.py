
def get_coin_balances(lst1, lst2):
  a, b = 3, 3
  for i, j in zip(lst1, lst2):
    if i == 'share':  a, b = a-1, b+3
    if j == 'share':  a, b = a+3, b-1
  return [a, b]

