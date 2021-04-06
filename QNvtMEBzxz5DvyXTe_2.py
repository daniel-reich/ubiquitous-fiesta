
def strong_password(password):
  if(len(password)>=6):
    length=True
  else:
    return 6-len(password)
  upper=False
  lower=False
  number=False
  special=False
  total=0
  for i in password:
    if(i in "abcdefghijklmnopqrstuvwxyz"):
      lower=True
    elif(i in "0123456789"):
      number=True
    elif(i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
      upper=True
    elif(i in "!@#$%^&*()-+"):
      special=True
  if(length and upper and lower and number and special):
    return 0
  if(length):
    total+=1
  if(upper):
    total+=1
  if(lower):
    total+=1
  if(number):
    total+=1
  if(special):
    total+=1
  return (5-total)

