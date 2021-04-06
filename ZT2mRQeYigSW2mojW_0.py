
import re
def haiku(string):
  lines = string.split('/')
  pat = r'[^aeiouy ]*[aeiouy]{1,3}[^aeiouy ]*(?:e\'?s?(?:\W|$))?'
  return [len(re.findall(pat,l,re.I)) for l in lines] == [5,7,5]

