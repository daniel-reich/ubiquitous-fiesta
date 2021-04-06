
from numpy import sort     
def alphabet_soup(txt):
  ordList = sort([ord(c) for c in txt])
  return ''.join([chr(d) for d in ordList])

