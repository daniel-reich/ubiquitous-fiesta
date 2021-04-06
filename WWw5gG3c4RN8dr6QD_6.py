
def after_n_months(year, month):
  if not year:
    return "year missing"
  if not month:
    return "month missing"
  else:
    return int(year + month/12)

