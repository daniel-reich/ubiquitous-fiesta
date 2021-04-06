
def get_prices(lst):
  import re
  return list(map(float,re.findall('\d+.\d+',''.join(lst))))

