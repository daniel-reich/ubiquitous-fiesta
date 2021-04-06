
def alphanumeric_restriction(s):
  isalpha = False
  isnum = False
  if len(s) == 0:
    return False
  for i in s:
    if i.isalpha() == True:
      isalpha = True
    elif i.isnumeric() == True:
      isnum = True
    else:
      return False
    if isalpha == True and isnum == True:
      return False
      
  return True

