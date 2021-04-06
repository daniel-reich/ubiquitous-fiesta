
def get_prices(lst):
  ret = []
  for x in lst:
    y = x.split('($')[1].split(')')[0]
    ret.append(float(y))
  return ret

