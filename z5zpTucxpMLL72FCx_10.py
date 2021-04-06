
import re
def grab_city(txt):
  txtregex = re.compile(r'\[([a-zA-z ]+)\]$')
  mo = txtregex.search(txt)
  return mo.group(1)

