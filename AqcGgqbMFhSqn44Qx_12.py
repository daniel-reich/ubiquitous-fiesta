
import re
​
def tweet(txt):
  pattern = '[@|#]{1}\w+'
  return ' '.join(re.findall(pattern, txt))

