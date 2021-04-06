
import re
def letters_only(txt):
  return ''.join(re.findall(r'[a-zA-Z]', txt))

