
def strong_password(password):
  if len(password)<6:
    return 6-len(password)
  count=0
  numbers = "0123456789"
  for i in numbers:
    if i in password:
      break
  else:
    count+=1
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  for i in lower_case:
    if i in password:
      break
  else:
    count+=1
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in upper_case:
    if i in password:
      break
  else:
    count+=1
  special_characters = "!@#$%^&*()-+"
  for i in special_characters:
    if i in password:
      break
  else:
    count+=1
  return count

