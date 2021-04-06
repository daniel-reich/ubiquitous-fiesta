
def is_repdigit(num):
  a=str(num)
  if num<0:
    return False
  elif num==0:
    return True
  else:
    for i in a:
      if i!=a[0]:
        return False
    return True

