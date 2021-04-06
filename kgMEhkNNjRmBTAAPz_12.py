
import re
def remove_special_characters(txt):
  reSp = re.sub(r'[^a-zA-Z0-9-_ ]',"",txt)
  return reSp

