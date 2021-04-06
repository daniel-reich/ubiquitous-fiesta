
import re
​
def validate(s):
  print("S: ", s)
  regx = p = re.compile('(?:\+?1[ \-.\/])?(?:\(?\d{3}\)?[ \-.\/](?:\d{3}[ \-.\/])?\d{4})$|(\d{10})')
  
  if(regx.match(s)):
    return True
  else:
    return False

