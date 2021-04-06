
import re
​
def ing_extractor(string):
  return re.findall(r"(?i)\S*[aeiou*]\S*ing", string)

