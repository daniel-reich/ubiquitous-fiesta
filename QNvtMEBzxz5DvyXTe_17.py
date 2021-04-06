
def strong_password(password):
  p=0
  sc='!@#$%^&*()-+'
  for i in password:
    if i.isnumeric():
      p|=1
    elif i.islower():
      p|=2
    elif i.isupper():
      p|=4
    elif i in sc:
      p|=8
  return max(6-len(password),4-bin(p).count('1'))

