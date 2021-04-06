
def make_change(c):
  change = {}
  change['q'], c = c // 25, c % 25
  change['d'], c = c // 10, c % 10
  change['n'], c = c // 5, c % 5
  change['p'] = c
  return change

