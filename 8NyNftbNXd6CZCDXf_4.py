
def get_coin_balances(lst1, lst2):
  A=[x for x in zip(lst1, lst2)]
  a, b=3, 3
  for x, y in A:
    if (x, y) == ('share', 'share'):
      a+=2
      b+=2
    elif (x, y) ==('share', 'steal'):
      a-=1
      b+=3
    elif (x, y) == ('steal', 'share'):  
      a+=3
      b-=1
    else:
      a+=0
      b+=0
  return [a,b]

