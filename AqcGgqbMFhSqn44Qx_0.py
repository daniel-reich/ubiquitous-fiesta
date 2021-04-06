
import re
def tweet(txt):
  return ' '.join(re.findall('[#@]\w+',txt))

