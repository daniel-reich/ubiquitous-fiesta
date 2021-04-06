
def after_n_months(year, month):
  return 'year missing' if year==None else ('month missing' if month==None else year+(month//12))

