
def who_wins_tonight(coins, space, price, size):
  bill, will = coins // price, space // size
  return 'Tie' if bill == will else ['Bill', 'Will'][will > bill]

