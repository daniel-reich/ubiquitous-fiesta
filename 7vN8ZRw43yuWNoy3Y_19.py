
import re
def parse_code(txt):
  items = re.split("0+", txt)
  return {"first_name": items[0], "last_name": items[1], "id": items[2]}

