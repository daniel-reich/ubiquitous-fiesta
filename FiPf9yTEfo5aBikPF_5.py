
def coins_combinations(money, coins, value=0):
  if value == money:
    return 1
  return sum(coins_combinations(money, coins[i:], value + coins[i]) \
          for i in range(len(coins))) if value < money else 0

