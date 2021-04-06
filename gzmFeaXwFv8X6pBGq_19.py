
def series_resistance(lst):
  ohm = sum(lst)
  return "{} ohm{}".format(ohm, "" if ohm <= 1 else "s")

