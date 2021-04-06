
def series_resistance(lst):
  return '{0} ohm{1}'.format(sum(lst),'s' if sum(lst)>1 else '')

