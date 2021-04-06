
def get_coin_balances(lst1, lst2):
  a, b, = 3, 3
  
  for i in lst1:
    if i == 'share':
      a -= 1
      b += 3
  
  for i in lst2:
    if i == 'share':
      b -= 1
      a += 3
    
  return [a,b]

