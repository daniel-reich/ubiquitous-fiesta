
def get_coin_balances(lst1, lst2):
  p1,p2 = 3,3
  for c1,c2 in zip(lst1,lst2):
    if c1=='share':
      p1-=1
      p2+=3
    if c2=='share':
      p2-=1
      p1+=3
  return [p1,p2]

