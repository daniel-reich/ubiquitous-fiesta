
import re
​
​
def ing_extractor(string):
  regex = r'[\w\*]+[aeuiou\*][\w]*ing'
  return re.findall(regex, string, re.IGNORECASE)

