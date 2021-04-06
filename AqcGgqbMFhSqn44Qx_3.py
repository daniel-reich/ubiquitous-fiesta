
import re
def tweet(txt):
  return " ".join(re.findall(r'[@#][A-Za-z]+', txt))

