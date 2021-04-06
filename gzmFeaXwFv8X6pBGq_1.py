
def series_resistance(lst):
  return "{} {}".format(sum(lst), "ohms" if sum(lst) > 1 else "ohm")

