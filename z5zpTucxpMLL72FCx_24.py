
from re import search
​
def grab_city(txt):
  return search(r'\[[\w ]+]$', txt).group(0)[1:-1]

