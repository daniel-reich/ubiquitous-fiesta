
def series_resistance(lst):
  res = sum(lst)
  return '{} ohm{}'.format(res, ['', 's'][res > 1])

