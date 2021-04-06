
def strong_password(password):
  to_fulfill = 0
  if len([i for i in password if i in '0123456789']) == 0: to_fulfill += 1
  if len([i for i in password if i.isupper()]) == 0: to_fulfill += 1
  if len([i for i in password if i.islower()]) == 0: to_fulfill += 1
  if len([i for i in password if i in '!@#$%^&*()-+']) == 0: to_fulfill += 1
  return max(6-len(password), to_fulfill)

