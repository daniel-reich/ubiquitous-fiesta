
def series_resistance(lst):
  return '{} ohm{}'.format(round(sum(lst), 1), ['', 's'][sum(lst) > 1])

