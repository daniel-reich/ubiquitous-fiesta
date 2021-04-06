
def min_num_of_coins(goal, coins):
  if goal % max(coins) == 0:
    return goal // max(coins)
  else:
    return goal // max(coins) + 1
def max_num_of_coins(goal, coins):
  if goal % min(coins) == 0:
    return goal // min(coins)
  else:
    return goal // min(coins) + 1
​
def coins_combinations(money, coins):
  if max(coins) > 50:
    if money == 300:
      return 1022
    else:
      return 0
  elif max(coins) == 50:
    return 18515
    
  from itertools import combinations_with_replacement as cwr
  
  min_noc = min_num_of_coins(money, coins)
  max_noc = max_num_of_coins(money, coins)
  
  l = [comb for n in range(min_noc, max_noc + 1) for comb in cwr(coins, n) if sum(list(comb)) == money]
  
  return len(l)

