
def afterNMonths(year,month):
  if year == None:
    return 'year missing'
  elif month == None:
    return 'month missing'
  else:
    diff = month // 12
    return year + diff

