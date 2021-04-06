
def is_valid_date(d, m, y):
  if m>12:
    return False
  if ( m==4 or m==6 or m==9 or m==11):
    if d>30:
      return False
    else:
      return True
  if m==2:
    if d>29:
      return False
    elif d>28:
      if (y%400==0 or y%4==0):
        if(y%100==0):
          return False
        else:
          return True
      return False
    return True
  elif d>31:
    return False
  else:
    return True

