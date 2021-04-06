
def share(lst):
  return len([i for i in lst if i == 'share'])
  
def get_coin_balances(lst1, lst2):
  player1 = share(lst2) * 3 + (3 - share(lst1))
  player2 = share(lst1) * 3 + (3 - share(lst2))
  return [player1, player2]

