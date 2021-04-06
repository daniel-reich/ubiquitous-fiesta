
def strong_password(password):
  tf = [False,False,False,False]
  ret = 4
  special_characters = "!@#$%^&*()-+"
  for x in password:
    if(x.isdigit()):
      tf[0] = True 
    if(x.islower()):
      tf[1] = True
    if(x.isupper()):
      tf[2] = True
    if(x in special_characters):
      tf[3] = True
  for y in tf:
    if(y == True):
      ret -= 1
  if(len(password) < 6):
    ret = 6 - len(password)
  return ret

