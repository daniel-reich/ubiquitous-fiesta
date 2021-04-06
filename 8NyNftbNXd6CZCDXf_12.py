
profit = {
  "share share": (2, 2), 
  "share steal": (-1, 3), 
  "steal share": (3, -1), 
  "steal steal": (0, 0)
}
​
from functools import reduce
def get_coin_balances(lst1, lst2):
  add_profit = lambda p1, p2: [p1[0]+p2[0], p1[1]+p2[1]]
  turns = (profit[p1 + " " + p2] for p1, p2 in zip(lst1, lst2))
  return reduce(add_profit, turns, [3, 3])

