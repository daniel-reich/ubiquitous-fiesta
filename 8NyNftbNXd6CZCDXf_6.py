
def get_coin_balances(lst1, lst2):
  red_total = 3
  blue_total = 3
  for i in range(len(lst1)):
    if lst1[i] == 'steal' and lst2[i] == 'share':
      red_total += 3
      blue_total -= 1
    elif lst1[i] == 'share' and lst2[i] == 'share':
      red_total += 2
      blue_total += 2
    elif lst1[i] == 'steal' and lst2[i] == 'steal':
      continue
    elif lst1[i] == 'share' and lst2[i] == 'steal':
      red_total -= 1
      blue_total += 3
  return [red_total,blue_total]

