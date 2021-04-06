
def series_resistance(lst):
  total = sum(lst)
  return '{} ohm{}'.format(total, 's' * (total > 1))

