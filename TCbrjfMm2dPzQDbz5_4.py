
import re
def insert_whitespace(txt):
  txt = re.findall('[\D][^A-Z]*',txt)
  return ' '.join(txt)

