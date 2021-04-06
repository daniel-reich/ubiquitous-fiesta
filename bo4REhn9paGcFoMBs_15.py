
def age_difference(ages):
  a, b  = sorted(ages)[-2:]
  diff  = b - a
  return "No age difference between spouses." if diff == 0 else '{} year{}'.format(diff, ('s', '')[diff == 1])

