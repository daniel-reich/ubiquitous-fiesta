
def series_resistance(lst):
  return '{} {}'. format(round(sum(lst),1), 'ohms' if sum(lst)>1 else 'ohm')

