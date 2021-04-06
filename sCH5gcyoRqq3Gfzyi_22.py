
def valid_str_number(n):
  import re
  if n.count('.')>1 or re.search("[a-z]",n):
    return False
  else:
    return True

