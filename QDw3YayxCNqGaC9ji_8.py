
def make_change(c):
  coin_to_penny = {
    'q': 25,
    'd': 10,
    'n': 5,
    'p': 1,
  }
  coins = ['q', 'd', 'n', 'p']
  change = {}
  for coin in coins:
    coin_count = c // coin_to_penny[coin]
    change[coin] = coin_count
    c -= coin_count * coin_to_penny[coin]
  return change

