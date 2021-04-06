
def afterNMonths(year,month):
  if month==None:
    return 'month missing'
  elif year==None:
    return 'year missing'
  if month<12:
    return year
  else:
    k=0
    k=month//12
    return year+k

