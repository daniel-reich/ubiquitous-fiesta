
def series_resistance(lst):
  return "{} ohms".format(sum(lst)) if sum(lst)>11 else "{} ohm".format(sum(lst));

