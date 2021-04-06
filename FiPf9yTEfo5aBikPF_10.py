
def coins_combinations(money, coins):
  coins = sorted(coins)
  if money == coins[0]:
    return 1
  elif money < coins[0]:
    return 0
  elif len(coins) > 1:
    return coins_combinations(money-coins[0], coins) \
          + coins_combinations(money, coins[1:])
  else:
    return money % coins[0] == 0

