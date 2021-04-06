
import re
​
def tweet(txt):
  return ' '.join(re.findall(r'[@#]\w+', txt))

