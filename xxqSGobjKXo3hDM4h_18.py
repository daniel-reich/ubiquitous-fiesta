
import re
def ing_extractor(string):
  return [group[0] for group in 
      re.findall(r'(\w*([aeiou]+|\*+)\w*ing)', string, re.I)]

