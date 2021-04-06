
def after_n_months(year, month):
    if year == None:
      return 'year missing'
    if month == None:
      return 'month missing'
    else:
      my = month // 12
      return year + my

