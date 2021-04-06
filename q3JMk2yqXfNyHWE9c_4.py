
import re
def double_letters(word):
  return re.search(r'([a-z])\1+',word, re.I) != None

