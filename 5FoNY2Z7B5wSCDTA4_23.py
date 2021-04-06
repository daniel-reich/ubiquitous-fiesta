
def happy_year(year):
  year += 1
  if len(set(str(year))) == len(str(year)):
    return year
  return happy_year(year)

