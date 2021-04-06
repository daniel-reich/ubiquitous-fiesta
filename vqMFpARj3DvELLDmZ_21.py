
import re
def letters_only(txt):
  txt = re.findall(r'[A-Za-z]', txt)
  return ''.join(txt)

