
def get_prices(lst):
  return [float(i.split('$')[1].split(')')[0]) for i in lst]

