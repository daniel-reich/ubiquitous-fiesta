
import re
def grab_city(txt):
  brackets = re.findall(r'\[[a-zA-Z ]+\]', txt)
  return brackets[-1][1:-1]

