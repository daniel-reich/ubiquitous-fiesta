
import math as m
​
def make_change(c):
  cnt = [0, 0, 0, 0]
  coins = [25, 10, 5, 1]  
  for x in range(0,4):
    cnt[x] = m.floor(c/coins[x])
    c -= cnt[x]*coins[x]
  return {'q': cnt[0], 'd': cnt[1], 'n': cnt[2], 'p': cnt[3]}

