
import re
def get_prices(lst):
  p=r'(?<=\$)[\d\.]+'
  return [float(re.search(p,x).group()) for x  in lst]

