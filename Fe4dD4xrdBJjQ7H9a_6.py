
def who_wins_tonight(coins, space, price, size):
  check = space//size - coins//price
  check = -1 if check < 0 else 1 if check > 0 else 0
  return ['Tie', 'Will', 'Bill'][check]

