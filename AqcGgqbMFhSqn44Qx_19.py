
from re import findall
def tweet(txt):
  return ' '.join(findall("[#@]\w*", txt))

