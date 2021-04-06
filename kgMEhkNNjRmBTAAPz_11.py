
import re
def remove_special_characters(txt):
  return ''.join(re.findall('([-_a-zA-Z0-9\s])', txt))

