
def series_resistance(lst):
  resistance = 0
  for value in lst:
    resistance += value
  if resistance <= 1:
    output = str(resistance) + " ohm"
    return output
  else:
    output = str(resistance) + " ohms"
    return output

