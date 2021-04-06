
def series_resistance(lst):
  return str(sum(lst)) + " ohm" if sum(lst) <= 1 else str(sum(lst)) + " ohms"

