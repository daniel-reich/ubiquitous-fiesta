
import re
def letters_only(s):
  return "".join(re.findall(r'[a-zA-Z]+',s))

