
def get_coin_balances(lst1, lst2):
  k, l = 3, 3
​
  for i, j in zip(lst1, lst2):
    if j == 'share':
      k += 3
      l -= 1
    if i == 'share':
      l += 3
      k -= 1
    if j == 'steal':
      k += 0
    if i == 'steal':
      l += 0
  
  return [k, l]

