
import re
def ing_extractor(string):
  return re.findall('[\w\*]*[aeiou\*]\w*ing', string, re.I)

