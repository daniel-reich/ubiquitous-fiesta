
def series_resistance(lst):
  return '{} ohm{}'.format(sum(lst), 's' if sum(lst)>1 else '')

