
def strong_password(password):
  special_chars = "!@#$%^&*()-+"
  if len(password) < 6:
    length = 6 - len(password)
  else:
    length = 0
  digits = list(filter(lambda x: x.isdigit(),password))
  special = list(filter(lambda x: x in special_chars,password))
  lower = list(filter(lambda x: x.islower(),password))
  upper = list(filter(lambda x: x.isupper(),password))
  
  amount = len(list(filter(lambda x: len(x) == 0, [digits,special,lower,upper])))
  return max(amount,length)

