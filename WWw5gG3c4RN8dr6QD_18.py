
def after_n_months(year, month):
  if year == None:
    return "year missing"
  elif month == None:
    return "month missing"
  else:
    return year + month // 12

