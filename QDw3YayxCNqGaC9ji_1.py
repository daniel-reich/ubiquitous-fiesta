
def make_change(c):
  ret = {}
  ret['q'], c = c // 25, c % 25
  ret['d'], c = c // 10, c % 10
  ret['n'], ret['p'] = c // 5, c % 5
  return ret

