
def get_prices(lst):
  import re
  return [float(''.join(re.findall('[0-9.]', x))) for x in lst]

