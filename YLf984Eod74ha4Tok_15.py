
def leap_year(yr):
  tail = int(str(yr)[2:])
  try:
    return not tail**2/tail % 4
  except:
    return not yr % 400

