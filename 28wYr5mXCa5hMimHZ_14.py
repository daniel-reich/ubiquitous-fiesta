
def valid_name(name):
  parts = name.split(' ')
  lastname = parts[-1]
  firstname = parts[0]
  middlename = None
​
  if len(parts) == 3:
    middlename = parts[1]
​
  if len(parts) not in [2,3]:
    return False
 
  #lastname
  if lastname[0] != lastname[0].upper():
    return False
  if len(lastname) < 2:
    return False
  if '.' in lastname:
    return False
​
  #firstname
  if firstname[0] != firstname[0].upper():
    return False
  if '.' in firstname and len(firstname) != 2:
    return False
  elif len(firstname) < 2:
    return False    
  #middlename
  if middlename:
    if '.' in firstname and '.' not in middlename:
      return False
    if middlename[0] != middlename[0].upper():
      return False
    if '.' in middlename and len(middlename) != 2:
      return False
    elif len(middlename) < 2:
      return False
  return True

