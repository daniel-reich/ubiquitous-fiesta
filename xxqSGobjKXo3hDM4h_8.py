
import re
def ing_extractor(string):
  return re.findall(r'(?i)[a-z\*]+[aeiou\*{2}][a-z\*]+ing',string)

