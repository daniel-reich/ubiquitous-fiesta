
import re
def markdown(s):
  return lambda x,y: re.sub("(%s[\.?!]*)"%(y),r"%s\1%s"%(s,s),x,flags=re.I)

