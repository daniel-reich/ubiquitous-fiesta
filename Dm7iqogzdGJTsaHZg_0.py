
import re
​
def retrieve(txt):
  return re.findall(r'\b[aeiou]\w*\b', txt.lower())

