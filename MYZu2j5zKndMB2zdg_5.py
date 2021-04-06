
import re
def absolute(txt):
  
  txt=re.sub('[aA]\s', "an absolute ", txt)
  return txt.capitalize()

