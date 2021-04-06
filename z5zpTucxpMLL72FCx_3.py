
import re
def grab_city(txt):
  return re.findall('\[.*?\]',txt)[-1][1:-1]

