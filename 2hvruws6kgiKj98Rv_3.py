
from re import sub
​
def to_scottish_screaming(txt):
  return sub('[AIOU]', 'E', txt.upper())

