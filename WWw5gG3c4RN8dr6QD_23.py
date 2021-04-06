
def after_n_months(year, month):
  return "year missing" if not year else "month missing" if not month else year + int(month/12)

