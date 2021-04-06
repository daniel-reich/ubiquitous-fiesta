
def letters_only(s):
  import re
  if s.islower() == False or re.search(r"\d",s) != None:
    return False
  else:
    return True

