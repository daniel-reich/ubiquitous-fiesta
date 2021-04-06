
def who_wins_tonight(coins, space, price, size):
  b, w = coins//price, space//size
  return ['Bill', 'Will', 'Tie'][[b > w, b < w, True].index(True)]

