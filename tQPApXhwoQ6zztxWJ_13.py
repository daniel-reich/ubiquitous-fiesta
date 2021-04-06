
import re
def get_prices(lst):
  s=''.join(lst)
  x= (re.findall(r'\d+\.\d{1,2}',s))
  return [float (i) for i in x]

