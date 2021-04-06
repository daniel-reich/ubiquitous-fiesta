
import re
def scrambled(words, mask):
  sr='^'+mask.replace('*','.')+'$'
​
  return sorted( [x for x in words if re.match(sr,x) ] )

