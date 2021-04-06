
def after_n_months(year, month):
  return "year missing" if year is None else "month missing" if month is None else round(year + (month / 12), 0)

