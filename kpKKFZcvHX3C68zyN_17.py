
def swap_cards(x, y):
  (a, b), (c, d) = sorted(divmod(x, 10)), divmod(y, 10)
  new = 10 * c + b if x % 10 == b else 10 * b + c
  return new > 10 * a + d

