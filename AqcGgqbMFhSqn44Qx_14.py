
import re
def tweet(txt):
  s = re.finditer(r'(@|#)\w*', txt)
  return ' '.join(x.group(0) for x in s)

