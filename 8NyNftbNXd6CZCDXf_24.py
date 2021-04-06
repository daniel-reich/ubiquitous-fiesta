
def get_coin_balances(lst1, lst2):
  p1,p2 = 3,3
  for i in range(len(lst1)):
    if lst1[i]=='share':
      if p1>0:
        p1-=1
        p2+=3
    if lst2[i]=='share':
      if p2>0:
        p2-=1
        p1+=3
  return [p1,p2]

