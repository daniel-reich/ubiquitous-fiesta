
import re
def get_prices(lst):
  pattern = re.compile ('\d+\.\d+')
  return [float(i) for i in re.findall (pattern, ''.join(lst))]

