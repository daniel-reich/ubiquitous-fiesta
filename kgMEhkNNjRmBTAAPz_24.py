
import re
def remove_special_characters(txt):
  pat = re.compile(r'[^\w\-\s]')
  return re.sub(pat,'',txt)

