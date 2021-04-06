
def series_resistance(lst):
  return str(sum(lst)) + " {}".format('ohm' if sum(lst) < 2 else 'ohms')

