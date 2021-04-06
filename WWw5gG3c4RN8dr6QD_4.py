
def after_n_months(year,month):
  if month == None:
    return 'month missing'
  return year + int(month/12) if year != None else 'year missing'

