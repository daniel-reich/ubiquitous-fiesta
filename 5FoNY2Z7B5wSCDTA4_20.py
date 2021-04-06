
def happy_year(year):
  next_year = year + 1
  if len(str(next_year)) == len(set(str(next_year))):
    return next_year
  else:
    return happy_year(year + 1)

