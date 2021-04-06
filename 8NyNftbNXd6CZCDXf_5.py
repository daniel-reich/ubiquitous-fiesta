
def get_coin_balances(r, b):
  x, y = 3, 3
  for i, _ in enumerate(r):
    x, y = [x+2, y] if r[i][:2] == 'sh' else [x+3, y-3];
    x, y = [x, y+2] if b[i][:2] == 'sh' else [x-3, y+3]
  return [x, y]

