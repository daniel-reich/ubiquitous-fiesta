
def is_heteromecic(n):
  if  n == 0:
    return True
  print (n)
  for i in range (0,n):
    if i * (i + 1) == n:
      return True
  else:
    return False

