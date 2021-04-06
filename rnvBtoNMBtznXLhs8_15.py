
def win_round(you, opp):
  double_digit = lambda x: ''.join(map(str, sorted(x)[:-3:-1]))
  return double_digit(you) > double_digit(opp)

