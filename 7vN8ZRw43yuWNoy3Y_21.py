
import re
def parse_code(txt):
  m = re.match(r'([a-zA-Z]+)0+([a-zA-Z]+)0+([1-9]+)', txt)
  return  {"first_name": m.group(1), "last_name": m.group(2),"id": m.group(3)}

