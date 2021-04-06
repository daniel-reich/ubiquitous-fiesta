
import re
def plus_sign(txt):
  return re.findall(r'[a-zA-Z]+', txt)==re.findall(r'(?<=\+)[a-zA-Z]+(?=\+)', txt)

