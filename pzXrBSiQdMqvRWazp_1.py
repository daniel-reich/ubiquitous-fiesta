
def score_calculator(e, m, h):
  return "invalid" if min([e,m,h]) < 0 else e * 5 + m * 10 + h * 20

