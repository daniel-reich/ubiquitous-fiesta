
import re
def remove_special_characters(txt):
  return re.sub(r'[^\w\s-]', '', txt)

