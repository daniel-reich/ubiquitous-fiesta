
import re
​
def letters_only(txt):
  return re.sub(r'[^a-zA-Z]', '', txt)

