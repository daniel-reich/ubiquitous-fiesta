
import re
def insert_whitespace(txt):
  return re.sub(r'([a-z])([A-Z])', '\g<1> \g<2>', txt)

