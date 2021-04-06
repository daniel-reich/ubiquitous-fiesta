
def who_wins_tonight(coins, space, price, size):
  bill_coins = coins // price
  will_invt = space // size
  if bill_coins == will_invt:
    return "Tie"
  if bill_coins > will_invt:
    return "Bill"
  return "Will"

