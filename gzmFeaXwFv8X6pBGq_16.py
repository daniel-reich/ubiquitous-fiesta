
def series_resistance(lst):
  ans = round(sum(lst), 1)
  return '{} ohm{}'.format(ans, ['', 's'][ans > 1])

