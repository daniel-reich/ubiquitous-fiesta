
def insert_whitespace(txt):
  import re
  return re.sub(r'(\w)([A-Z])',r'\1 \2',txt)

