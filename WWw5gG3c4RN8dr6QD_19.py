
def afterNMonths(year,month):
  if year is None:
    return 'year missing'
  if month is None:
    return 'month missing'
  return year + month//12

