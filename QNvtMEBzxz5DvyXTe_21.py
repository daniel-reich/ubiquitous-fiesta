
import re
def strong_password(s):
  s1="\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\+ [a-z] [A-Z] \d";c=0
  for i in s1.split():
    if re.search(i,s):
      pass
    else:
      c=c+1
  if c+len(s)<6:
    return c+(6-(c+len(s)))
  else:
    return c

