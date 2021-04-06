
def valid_division(d):
  ss = d.split('/')
  if int(ss[1]) == 0:
    return 'invalid'
  elif (int(ss[0]) % int(ss[1]))== 0:
    return True
  else:
    return False

