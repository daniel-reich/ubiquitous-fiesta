
import re
def ing_extractor(string):
  return [w for w in string.split() if re.match('^.*[aeiou*].*ing$', w, re.IGNORECASE)]

