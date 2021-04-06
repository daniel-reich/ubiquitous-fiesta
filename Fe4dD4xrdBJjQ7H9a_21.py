
def who_wins_tonight(coins, space, price, size):
  b, w = coins//price, space//size
  return "Will" if w > b else "Bill" if b > w else "Tie"

