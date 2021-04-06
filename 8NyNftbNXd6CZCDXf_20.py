
def get_coin_balances(a, b):
  key = {
    ('share', 'share'): (2, 2),
    ('steal', 'steal'): (0, 0),
    ('share', 'steal'): (-1, 3),
    ('steal', 'share'): (3, -1),
  }
  game = [3, 3]
  for i, j in zip(a, b):
    match = key[(i, j)]
    game[0] += match[0]
    game[1] += match[1]
  return game

