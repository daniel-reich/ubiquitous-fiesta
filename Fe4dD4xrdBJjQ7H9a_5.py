
def who_wins_tonight(coins, space, price, size):
  if coins//price > space//size:
    return "Bill"
  elif space//size > coins//price:
    return "Will"
  return "Tie"

