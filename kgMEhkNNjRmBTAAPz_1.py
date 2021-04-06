
import re
def remove_special_characters(txt):
  return re.sub('[^\s\-\w_]', '', txt)

