
import re
def ing_extractor(string):
  return re.findall(r"[\w*]+[*aeoiu]\w+ing", string, re.I)

