
import re
def remove_special_characters(txt):
  return ''.join(re.findall('\w|\s|-|_', txt))

