
def swap_cards(x, y):
  [a, b, c, d] = map(int, str(x) + str(y))
  return [c*10+b > a*10+d, a*10+c > b*10+d][a > b]

