
import re
def grab_city(txt):
  return re.search("\[([\w\s]+)\]$", txt).group(1)

