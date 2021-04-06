
def secret(num):
  t,u = divmod(num, 10)
  return t**u - t*u

