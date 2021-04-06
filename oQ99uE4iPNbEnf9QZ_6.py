
def no_perms_digits(n):
  retVal = 1
  for i in range(1,n+1):
    retVal *= i
  return len(str(retVal))

