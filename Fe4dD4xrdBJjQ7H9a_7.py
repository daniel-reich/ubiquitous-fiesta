
def who_wins_tonight(coins, space, price, size):
  bill = coins // price
  will = space // size
  return "Bill" if bill > will else "Will" if will > bill else "Tie"

