
import re
def grab_city(txt):
  return re.findall(r'\[(.*?)\]', txt)[-1]

