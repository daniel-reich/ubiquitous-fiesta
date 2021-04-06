
def strong_password(password):
  length = max(6 - len(password), 0)
  digit = 1 - any(i.isdigit() for i in password)
  lower = 1 - any(i.islower() for i in password)
  upper = 1 - any(i.isupper() for i in password)
  symbol = 1 - any(i in '!@#$%^&*()-+' for i in password)
  return max(length, digit+lower+upper+symbol)

