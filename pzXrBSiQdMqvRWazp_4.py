
def score_calculator(e, m, h):
  if all(i>=0 for i in [e, m, h]):
    return 5*e + 10*m + 20*h
  return "invalid"

