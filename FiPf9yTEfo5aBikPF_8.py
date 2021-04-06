
def coins_combinations(target, coins):
  ways = [1] + [0] * target
  for coin in coins:
    for i in range(coin, target + 1):
      ways[i] += ways[i - coin]
  return ways[target]

