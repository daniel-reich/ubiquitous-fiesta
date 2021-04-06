
import re
def get_prices(lst):
  return [float(x) for x in re.findall('(\d+\.\d+)', ''.join(x for x in lst))]

