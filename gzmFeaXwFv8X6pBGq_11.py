
def series_resistance(lst):
  a = ' ohms'
  b = ' ohm'
  c = sum(lst)
  if c <= 1:
    return str(c)+b
  else:
    return str(c) + a

