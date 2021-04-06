
def strong_password(password):
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"
  n = 0
  
  n = n+1 if not contains(password,numbers) else n
  n = n+1 if not contains(password,lower_case) else n
  n = n+1 if not contains(password,upper_case) else n
  n = n+1 if not contains(password,special_characters) else n
  
  if len(password)+n < 6:
    n = 6-len(password)
    
  return n
  
def contains(password, container):
  for p in password:
    if p in container: return True
  return False

