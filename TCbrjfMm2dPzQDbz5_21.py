
import re
def insert_whitespace(txt):
  return re.sub(r'([a-z])([A-Z])', '\\1 \\2', txt)

