
def century(year):
  if year % 100 == 0:
    century = year/100
  else:
    century = year//100 + 1
  
  if century < 21:
    return "%dth century" % century
  else:
    return "%dst century" % century

