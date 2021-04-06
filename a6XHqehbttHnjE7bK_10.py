
def is_repdigit(num):
  if num == 0:
    return True
  elif num < 0:
    return False
  else:
    dig = num%10
    while(num>1):
      if dig != num%10:
        return False
      num = num//10
    return True

