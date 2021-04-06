
import re
def double_letters(word):
  s=""
  s=re.search(r'((\w)\2)', word)
  if(s == None):
    return False
  else:
    return True

