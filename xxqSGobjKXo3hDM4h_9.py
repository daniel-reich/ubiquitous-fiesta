
import re
def ing_extractor(string):
  res = []
  pattern = re.compile(r'\w.*?[aeiou\*][^aeiou\s]+?ing',re.I)
  for s in string.split():
    if pattern.match(s):
      res.append(s)
    
  return res

