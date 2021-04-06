
def get_prices(lst):
  prices = []
  for i in lst:
    begin = i.index('(') + 2
    end = i.index(')')
    prices.append(float(i[begin:end]))
  return prices

