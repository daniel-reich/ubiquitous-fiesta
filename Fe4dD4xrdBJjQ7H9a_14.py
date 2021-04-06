
import math
def who_wins_tonight(coins, space, price, size):
  if math.floor(coins / price) > math.floor(space / size):
    return 'Bill'
  elif math.floor(coins / price) < math.floor(space / size):
    return 'Will'
  elif math.floor(coins/price) == math.floor(space/size):
    return 'Tie'

