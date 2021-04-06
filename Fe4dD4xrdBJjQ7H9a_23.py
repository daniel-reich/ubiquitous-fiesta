
def who_wins_tonight(coins, space, price, size):
  b = coins // price
  w = space // size
  return "Bill" if b > w else "Tie" if b == w else "Will"

