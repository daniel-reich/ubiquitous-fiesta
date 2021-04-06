
def series_resistance(lst):
  return '{} ohm'.format(sum(lst))+'s'*(sum(lst)>1)

