
import re
​
def get_prices(lst):
  return [float(i) for i in re.findall(r'\d+\.\d+', str(lst))]

