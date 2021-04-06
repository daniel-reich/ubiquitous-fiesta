
def who_wins_tonight(coins, space, price, size):
  will =int(space/size)
  bill = int(coins/price)
  if will > bill:
     return "Will"
  elif will < bill:
     return "Bill"
  return "Tie"

