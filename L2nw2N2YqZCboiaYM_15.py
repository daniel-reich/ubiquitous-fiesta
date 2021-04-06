
import re
def repeated(s):
  p=r'(\w{2,})\1{2,}'
  return bool(re.match(p,s)) or quit()

