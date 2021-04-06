
def get_coin_balances(lst1, lst2):
  share1 = lst1.count('share')
  share2 = lst2.count('share')
  return [3+share2*3-share1, 3+share1*3-share2]

