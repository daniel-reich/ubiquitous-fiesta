
def coins_combinations(m, lst, i=0):
  if m <= 0:
    return 1 if not m else None
​
  tot = 0
​
  for i in range(i, len(lst)):
    coin = lst[i]
    c = coins_combinations(m - coin, lst, (i, i+1)[m - coin < coin])
    tot += c if c else 0
​
  return tot

