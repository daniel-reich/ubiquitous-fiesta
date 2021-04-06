
def who_wins_tonight(coins, space, price, size):
  bill = lambda coins, price: coins // price
  will = lambda space, size: space // size
  
  return 'Will' if will(space, size) > bill(coins, price) else ['Bill', 'Tie'][will(space, size) == bill(coins, price)]

