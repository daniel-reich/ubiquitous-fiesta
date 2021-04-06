
def who_wins_tonight(coins, space, price, size):
  bill = coins // price
  will = space // size
  if bill > will: return "Bill"
  if bill < will: return "Will"
  return "Tie"

