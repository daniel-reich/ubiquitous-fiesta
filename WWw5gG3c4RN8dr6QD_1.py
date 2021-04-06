
def after_n_months(year, month):
  if not year:
    return 'year missing'
  if not month:
    return 'month missing'
  return year + month // 12

