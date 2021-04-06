
import re
def insert_whitespace(txt):
  return ' '.join(re.findall('[A-Z][a-z]*',txt))

