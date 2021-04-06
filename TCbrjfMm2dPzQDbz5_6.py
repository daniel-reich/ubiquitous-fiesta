
import re
def insert_whitespace(txt):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

