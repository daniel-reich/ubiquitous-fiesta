
import re
​
def tweet(txt):
  x = re.findall(r'[@#]{1}\w+', txt)
  return " ".join(x)

