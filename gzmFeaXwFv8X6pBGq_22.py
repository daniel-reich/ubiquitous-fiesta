
def series_resistance(lst):
  ohm = 0
  for x in lst:
      ohm += x
  
  ohm = round(ohm,1)
  
  if ohm <= 1:
    return str(ohm) + ' ohm'
  else:
    return str(ohm) + ' ohms'

