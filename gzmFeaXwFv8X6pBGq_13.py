
def series_resistance(lst):
  sum = 0
  for i in lst:
    sum += i
  
  if sum <= 1:
    return str(sum) + ' ohm'
  else:
    return str(sum) + ' ohms'

