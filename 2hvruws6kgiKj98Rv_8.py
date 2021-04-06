
import re
def to_scottish_screaming(txt):
  return re.sub('[AEIOU]','E',txt.upper())

