
from functools import reduce
def unstretch(word):
  return reduce(lambda x,y: x if x[-1:]==y else x+y, word)

