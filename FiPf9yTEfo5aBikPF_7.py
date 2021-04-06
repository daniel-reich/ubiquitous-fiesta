
def coins_combinations(money, coins):
  res = [0]*(money+1)
  res[0] = 1
  for c in coins:
    for j in range(len(res)):
      res[j] += res[j-c] if c <= j else 0
  return res[money]

