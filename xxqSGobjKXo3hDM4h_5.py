
import re
​
def ing_extractor(txt):
  return re.findall(r'\b[\w]+[aeiou*]+[\w*]+ing\b', txt, re.I)

