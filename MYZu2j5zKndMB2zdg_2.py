
import re
def absolute(txt):
  return re.sub(r'\ba\b', 'an absolute', txt.lower()).capitalize()

