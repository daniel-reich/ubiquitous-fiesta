
def get_prices(lst):
  return [float(i[i.index('(') + 2:-1]) for i in lst]

