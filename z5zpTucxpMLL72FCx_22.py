
import re
def grab_city(txt):
  extract = re.findall('\[(.*?)\]', txt)
  return extract[-1]

