
def after_n_months(year, month):
  if year == None:
    return "year missing"
  elif month == None:
    return "month missing"
  elif month > 12:
    s= month/12
    return year + round(s,0)
  else:
    return year

